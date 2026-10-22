
from pathlib import Path
import pandas as pd

BASE = Path(r"D:\Kho_du_lieu\Flood_DSS")

flood_path = BASE / (
    "02_Staging_CSV/Integrated/"
    "Flood_Water_Population_Reviewed.csv"
)

roads_path = BASE / (
    "02_Staging_CSV/Roads/"
    "Flood_Roads_Nearest.csv"
)

output_path = BASE / (
    "02_Staging_CSV/Integrated/"
    "Flood_Water_Population_Roads.csv"
)

log_path = BASE / (
    "07_Logs/Roads_Integration_Report.txt"
)

# 1. Đọc dữ liệu
flood = pd.read_csv(flood_path, encoding="utf-8-sig")
roads = pd.read_csv(roads_path, encoding="utf-8-sig")

print("=== ROAD INTEGRATION ===")
print("Flood rows:", len(flood))
print("Road nearest rows:", len(roads))

# 2. Kiểm tra các cột bắt buộc
required_flood = {"OBJECTID"}
required_roads = {
    "OBJECTID",
    "OBJECTID_2",
    "road_name",
    "Mentioned_years",
    "distance"
}

if not required_flood.issubset(flood.columns):
    raise ValueError("Flood thieu cot OBJECTID")

missing = required_roads - set(roads.columns)
if missing:
    raise ValueError(f"Roads thieu cot: {sorted(missing)}")

# 3. Kiểm tra khóa ghép
if flood["OBJECTID"].isna().any():
    raise ValueError("Flood co OBJECTID NULL")

if roads["OBJECTID"].isna().any():
    raise ValueError("Roads co OBJECTID NULL")

if flood["OBJECTID"].duplicated().any():
    raise ValueError("Flood co OBJECTID trung")

if roads["OBJECTID"].duplicated().any():
    raise ValueError("Roads co OBJECTID trung")

if len(flood) != 425 or len(roads) != 425:
    raise ValueError("So dong khong dung 425")

# 4. Chuẩn hóa trường khoảng cách
roads["distance"] = pd.to_numeric(
    roads["distance"], errors="raise"
)

if roads["distance"].isna().any():
    raise ValueError("Khoang cach co NULL")

if (roads["distance"] < 0).any():
    raise ValueError("Khoang cach am")

# 5. Chọn các trường cần tích hợp
road_selected = roads[[
    "OBJECTID",
    "OBJECTID_2",
    "road_name",
    "Mentioned_years",
    "distance"
]].copy()

road_selected = road_selected.rename(columns={
    "OBJECTID_2": "Nearest_Road_ID",
    "road_name": "Nearest_Road_Name",
    "Mentioned_years": "Nearest_Road_Mentioned_Years",
    "distance": "DistanceToNearestRoad_m"
})

# 6. Kiểm tra tránh ghi đè cột đã có
new_columns = set(road_selected.columns) - {"OBJECTID"}
conflicts = new_columns.intersection(flood.columns)

if conflicts:
    raise ValueError(f"Cot da ton tai: {sorted(conflicts)}")

# 7. Ghép theo OBJECTID
integrated = flood.merge(
    road_selected,
    on="OBJECTID",
    how="left",
    validate="one_to_one",
    indicator=True
)

if not integrated["_merge"].eq("both").all():
    raise ValueError("Co diem ngap khong ghep duoc Roads")

integrated = integrated.drop(columns=["_merge"])

# 8. Phân loại khoảng cách (chỉ để khảo sát)
def classify_distance(value):
    if pd.isna(value):
        return "Unknown"
    if value <= 50:
        return "0-50m"
    if value <= 100:
        return "50-100m"
    if value <= 500:
        return "100-500m"
    if value <= 1000:
        return "500-1000m"
    if value <= 5000:
        return "1000-5000m"
    return "Over_5000m"

integrated["Road_Distance_Band"] = (
    integrated["DistanceToNearestRoad_m"]
    .apply(classify_distance)
)

# 9. Trạng thái: chỉ xác nhận tìm được đường gần nhất
integrated["Road_Match_Status"] = (
    "Nearest_Only_Not_Confirmed"
)

# 10. Kiểm tra bảo toàn dữ liệu
if len(integrated) != len(flood):
    raise ValueError("So dong bi thay doi")

if not integrated["OBJECTID"].equals(flood["OBJECTID"]):
    raise ValueError("Thu tu OBJECTID bi thay doi")

original_columns = flood.columns.tolist()

pd.testing.assert_frame_equal(
    integrated[original_columns].reset_index(drop=True),
    flood.reset_index(drop=True),
    check_dtype=True
)

# 11. Xuất dữ liệu
output_path.parent.mkdir(parents=True, exist_ok=True)
log_path.parent.mkdir(parents=True, exist_ok=True)

integrated.to_csv(
    output_path,
    index=False,
    encoding="utf-8-sig"
)

# 12. Báo cáo
counts = integrated["Road_Distance_Band"].value_counts()

report = [
    "ROADS INTEGRATION REPORT",
    f"Input Flood: {len(flood)}",
    f"Input Road Nearest: {len(roads)}",
    f"Output: {len(integrated)}",
    f"Unique OBJECTID: {integrated['OBJECTID'].nunique()}",
    f"Missing road distances: {integrated['DistanceToNearestRoad_m'].isna().sum()}",
    "",
    "DISTANCE DISTRIBUTION",
    counts.to_string(),
    "",
    "Nearest road is NOT a confirmed flooded road.",
    "Mentioned_Years is NOT FloodCount.",
    f"Output file: {output_path}"
]

log_path.write_text(
    "\n".join(report),
    encoding="utf-8"
)

print("\n".join(report))


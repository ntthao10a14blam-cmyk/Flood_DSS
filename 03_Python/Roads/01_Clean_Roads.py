
from pathlib import Path
import pandas as pd

BASE = Path(r"D:\Kho_du_lieu\Flood_DSS")

input_path = BASE / "02_Staging_CSV/Roads/Roads_Raw.csv"
output_path = BASE / "02_Staging_CSV/Roads/Roads_Clean.csv"
log_path = BASE / "07_Logs/Roads_Cleaning_Report.txt"

# 1. Đọc dữ liệu
df = pd.read_csv(input_path, encoding="utf-8-sig")

print("=== KIEM TRA ROADS ===")
print("So dong:", len(df))
print("So cot:", len(df.columns))

# 2. Kiểm tra các cột bắt buộc
required = ["OBJECTID", "road_name", "Mentioned_years"]

missing_columns = set(required) - set(df.columns)

if missing_columns:
    raise ValueError(
        f"Thieu cot: {sorted(missing_columns)}"
    )

# 3. Kiểm tra mã đối tượng
if df["OBJECTID"].isna().any():
    raise ValueError("OBJECTID co gia tri NULL")

if df["OBJECTID"].duplicated().any():
    raise ValueError("OBJECTID bi trung")

# 4. Chuẩn hóa tên đường
df["road_name"] = (
    df["road_name"]
    .astype("string")
    .str.strip()
    .str.replace(r"\s+", " ", regex=True)
)

# 5. Kiểm tra tên đường
if df["road_name"].isna().any():
    raise ValueError("Co ten duong NULL")

if df["road_name"].eq("").any():
    raise ValueError("Co ten duong rong")

# 6. Chuẩn hóa số năm được đề cập
df["Mentioned_years"] = pd.to_numeric(
    df["Mentioned_years"],
    errors="raise"
)

if df["Mentioned_years"].isna().any():
    raise ValueError("Mentioned_years co NULL")

if (df["Mentioned_years"] < 0).any():
    raise ValueError("Mentioned_years co gia tri am")

if (
    df["Mentioned_years"]
    % 1 != 0
).any():
    raise ValueError("Mentioned_years khong phai so nguyen")

# 7. Kiểm tra tên đường trùng
duplicate_names = df["road_name"].duplicated().sum()

# 8. Chuẩn hóa tên cột
clean = df.rename(columns={
    "OBJECTID": "Road_ID",
    "road_name": "Road_Name",
    "Mentioned_years": "Mentioned_Years"
})

# 9. Bổ sung thông tin nguồn
clean["Source_ID"] = "ROAD_GPKG_01"

# 10. Chọn các cột đưa vào Staging
clean = clean[[
    "Road_ID",
    "Road_Name",
    "Mentioned_Years",
    "Source_ID"
]]

# 11. Kiểm tra bảo toàn bản ghi
assert len(clean) == len(df)
assert clean["Road_ID"].is_unique

# 12. Xuất CSV
output_path.parent.mkdir(parents=True, exist_ok=True)
log_path.parent.mkdir(parents=True, exist_ok=True)

clean.to_csv(
    output_path,
    index=False,
    encoding="utf-8-sig"
)

report = [
    "ROADS CLEANING QUALITY REPORT",
    f"Input rows: {len(df)}",
    f"Output rows: {len(clean)}",
    f"Missing values: {int(clean.isna().sum().sum())}",
    f"Duplicate Road_ID: {int(clean['Road_ID'].duplicated().sum())}",
    f"Duplicate road names: {int(duplicate_names)}",
    f"Min Mentioned_Years: {clean['Mentioned_Years'].min()}",
    f"Max Mentioned_Years: {clean['Mentioned_Years'].max()}",
    "Note: Mentioned_Years is not equivalent to FloodCount.",
    f"Output: {output_path}"
]

log_path.write_text(
    "\n".join(report),
    encoding="utf-8"
)

print("\n".join(report))

print("\n=== ROADS CLEAN ===")
print(clean.to_string(index=False))


import pandas as pd
from pathlib import Path

BASE = Path(r"D:\Kho_du_lieu\Flood_DSS")

input_file = BASE / "02_Staging_CSV" / "Flood_GIS_Raw.csv"
output_file = BASE / "02_Staging_CSV" / "Flood_Clean.csv"
report_file = BASE / "07_Logs" / "Flood_Quality_Report.csv"

df = pd.read_csv(input_file, encoding="utf-8-sig")

# 1. Kiểm tra các cột bắt buộc
required = [
    "OBJECTID", "Obs_id", "Date", "Year",
    "Location_name", "Longitude", "Latitude",
    "Water_height_min_cm", "Water_height_max_cm"
]

missing = [col for col in required if col not in df.columns]

if missing:
    raise ValueError(f"Thiếu các cột: {missing}")

# 2. Giữ nguyên mã nguồn và chuẩn hóa chuỗi
text_columns = [
    "Obs_id", "Location_name", "Location_type",
    "District_mentioned", "Ward", "Current_admin_unit",
    "Depth_class", "Cause", "Impact_type",
    "Source_id", "Source_type",
    "Spatial_precision", "Geocoding_method",
    "Observation_notes", "Commune", "Province"
]

for col in text_columns:
    if col in df.columns:
        df[col] = df[col].astype("string").str.strip()
        df[col] = df[col].replace("", pd.NA)

# 3. Chuẩn hóa ngày
# File GPKG xuất CSV thường có dạng YYYY-MM-DD HH:MM:SS
df["Date"] = pd.to_datetime(
    df["Date"],
    errors="coerce"
)

df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")

# 4. Chuẩn hóa dữ liệu số
numeric_columns = [
    "OBJECTID", "Year",
    "Water_height_min_cm", "Water_height_max_cm",
    "Duration_hours", "Longitude", "Latitude"
]

for col in numeric_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# 5. Gắn cờ chất lượng dữ liệu
df["Missing_Date"] = df["Date"].isna()

df["Missing_Depth"] = (
    df["Water_height_min_cm"].isna()
    & df["Water_height_max_cm"].isna()
)

df["Duplicate_Obs_id"] = df["Obs_id"].duplicated(
    keep=False
)

df["Invalid_Coordinates"] = (
    ~df["Longitude"].between(-180, 180)
    | ~df["Latitude"].between(-90, 90)
)

df["Invalid_Depth_Range"] = (
    df["Water_height_min_cm"].notna()
    & df["Water_height_max_cm"].notna()
    & (
        df["Water_height_min_cm"]
        > df["Water_height_max_cm"]
    )
)

# 6. Kiểm tra năm có khớp ngày không
parsed_dates = pd.to_datetime(df["Date"], errors="coerce")

df["Year_Date_Mismatch"] = (
    parsed_dates.notna()
    & df["Year"].notna()
    & (parsed_dates.dt.year != df["Year"])
)

# 7. Kiểm tra OBJECTID có duy nhất không
if df["OBJECTID"].isna().any():
    raise ValueError("Có OBJECTID bị thiếu")

if df["OBJECTID"].duplicated().any():
    raise ValueError("Có OBJECTID bị trùng")

# 8. Lưu dữ liệu đã chuẩn hóa
output_file.parent.mkdir(parents=True, exist_ok=True)
report_file.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(output_file, index=False, encoding="utf-8-sig")

# 9. Báo cáo chất lượng
quality_columns = [
    "Missing_Date", "Missing_Depth",
    "Duplicate_Obs_id", "Invalid_Coordinates",
    "Invalid_Depth_Range", "Year_Date_Mismatch"
]

report = pd.DataFrame({
    "Check": quality_columns,
    "Affected_Rows": [
        int(df[col].sum()) for col in quality_columns
    ]
})

report.to_csv(report_file, index=False, encoding="utf-8-sig")

print("=== KET QUA ETL ===")
print("So ban ghi:", len(df))
print("\nBao cao chat luong:")
print(report.to_string(index=False))
print("\nFile du lieu:", output_file)
print("File bao cao:", report_file)



from pathlib import Path
import pandas as pd

base = Path(r"D:\Kho_du_lieu\Flood_DSS")

source = base / "02_Staging_CSV/Integrated/Flood_Water_Population.csv"
output = base / "02_Staging_CSV/Integrated/Flood_Water_Population_Reviewed.csv"

df = pd.read_csv(source, encoding="utf-8-sig")

assert len(df) == 425, "So dong khong dung 425"
assert df["OBJECTID"].is_unique, "OBJECTID bi trung"

mask = df["OBJECTID"] == 184

assert mask.sum() == 1, "Khong tim thay duy nhat OBJECTID 184"

# Thông tin kiểm tra bổ sung, không thay đổi kết quả ghép gốc
df["Nearest_Area_ID"] = pd.NA
df["DistanceToNearestDistrict_m"] = pd.NA
df["Population_Review_Note"] = pd.NA

df.loc[mask, "Nearest_Area_ID"] = 776
df.loc[mask, "DistanceToNearestDistrict_m"] = 0.5193897529470466

df.loc[mask, "Population_Join_Status"] = "Boundary_Review"

df.loc[mask, "Population_Review_Note"] = (
    "Diem gan ranh gioi Quan 8 (0.52 m); "
    "chua xac nhan thuoc polygon Population 2019."
)

df.to_csv(output, index=False, encoding="utf-8-sig")

print("=== POPULATION BOUNDARY REVIEW ===")
print("Tong dong:", len(df))
print("OBJECTID 184:")
print(df.loc[mask, [
    "OBJECTID",
    "Population_Area_ID",
    "Nearest_Area_ID",
    "DistanceToNearestDistrict_m",
    "Population_Join_Status"
]].to_string(index=False))

print("\nTrang thai ghep:")
print(df["Population_Join_Status"].value_counts())
print("\nOutput:", output)


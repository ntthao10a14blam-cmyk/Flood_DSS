
from pathlib import Path
import pandas as pd

ROOT = Path(r"D:\Kho_du_lieu\Flood_DSS")
BASE = ROOT / "02_Staging_CSV"
LOGS = ROOT / "07_Logs"

input_file = BASE / "Integrated/Flood_Integrated_Staging.csv"
population_file = BASE / "Population/Population_Clean.csv"

output_file = (
    BASE / "Integrated/Flood_Integrated_Reviewed.csv"
)

report_file = LOGS / "Population_Boundary_Review.csv"

flood = pd.read_csv(input_file, dtype="string")
population = pd.read_csv(population_file, dtype="string")

# Tim su kien can kiem tra
mask = flood["Obs_ID"].eq("Obs_184")

if mask.sum() != 1:
    raise ValueError("Khong tim thay duy nhat Obs_184")

# Tim khu vuc Quan 8
area = population.loc[
    population["Area_ID"].eq("776")
]

if len(area) != 1:
    raise ValueError("Khong tim thay duy nhat Area_ID 776")

area = area.iloc[0]

# Xac minh cac dieu kien
event = flood.loc[mask].iloc[0]

if str(event["Year"]) != "2002":
    raise ValueError("Nam su kien khong khop")

nearest_area_id = pd.to_numeric(
    event["Nearest_Area_ID"],
    errors="coerce"
)

if pd.isna(nearest_area_id) or nearest_area_id != 776:
    raise ValueError(
        "Ma khu vuc gan nhat khong khop: "
        + str(event["Nearest_Area_ID"])
    )

if str(event["Population_Join_Status"]) != "Boundary_Review":
    raise ValueError("Trang thai khong dung")

distance = float(event["DistanceToNearestDistrict_m"])

if distance > 1:
    raise ValueError("Khoang cach vuot nguong kiem tra")

# Gan thong tin dan so co dieu kien
flood.loc[mask, "Population_Area_ID"] = area["Area_ID"]
flood.loc[mask, "Population_Area_Name"] = area["Area_Name"]
flood.loc[mask, "Population_ReferenceYear"] = area["Year"]
flood.loc[mask, "Population_BoundaryVersion"] = area["BoundaryVersion"]
flood.loc[mask, "Population_2019"] = area["Population"]
flood.loc[mask, "Population_Area_km2"] = area["Area_km2"]
flood.loc[mask, "PopulationDensity_2019"] = area["PopulationDensity"]

flood.loc[
    mask, "Population_Join_Status"
] = "Boundary_Assigned_Review"

flood.loc[
    mask, "Population_Review_Note"
] = (
    "Obs_184: Gan Quan 8 (Area_ID 776) theo "
    "ten dia diem va khu vuc gan nhat; "
    "cach ranh gioi 0.52 m. "
    "Can xac minh GIS truoc khi chap nhan chinh thuc."
)

# Giu nguyen trang thai chat luong su kien
# Khong sua DataQualityStatus

flood.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)

flood.loc[mask, [
    "OBJECTID",
    "Obs_ID",
    "Population_Area_ID",
    "Population_Area_Name",
    "Population_Join_Status",
    "Population_Review_Note"
]].to_csv(
    report_file,
    index=False,
    encoding="utf-8-sig"
)

print("===== REVIEW POPULATION BOUNDARY =====")
print("Tong dong:", len(flood))
print(
    "Thieu Population_Area_ID:",
    flood["Population_Area_ID"].isna().sum()
)
print("\nTrang thai Obs_184:")
print(
    flood.loc[mask, [
        "Obs_ID",
        "Population_Area_ID",
        "Population_Area_Name",
        "Population_Join_Status"
    ]].to_string(index=False)
)
print("\nDa luu:", output_file)

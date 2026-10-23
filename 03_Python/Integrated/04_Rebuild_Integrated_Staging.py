
from pathlib import Path
import pandas as pd

# ==================================================
# 1. KHAI BAO DUONG DAN
# ==================================================

ROOT = Path(r"D:\Kho_du_lieu\Flood_DSS")
BASE = ROOT / "02_Staging_CSV"
LOGS = ROOT / "07_Logs"

new_file = BASE / "Flood/Flood_Events_Staging.csv"
mapping_file = LOGS / "Flood_Old_New_ID_Mapping.csv"
integrated_file = (
    BASE / "Integrated/Flood_Water_Population_Roads.csv"
)

output_file = (
    BASE / "Integrated/Flood_Integrated_Staging.csv"
)

report_file = LOGS / "Integrated_Staging_Report.txt"

# ==================================================
# 2. DOC DU LIEU
# ==================================================

new = pd.read_csv(new_file, dtype="string")
mapping = pd.read_csv(mapping_file, dtype="string")
old_integrated = pd.read_csv(
    integrated_file,
    dtype="string"
)

print("===== DOC DU LIEU =====")
print("Flood New:", len(new))
print("Mapping:", len(mapping))
print("Old Integrated:", len(old_integrated))

# ==================================================
# 3. KIEM TRA DU LIEU DAU VAO
# ==================================================

if len(new) != 425:
    raise ValueError("Flood New khong du 425 dong")

if len(mapping) != 425:
    raise ValueError("Mapping khong du 425 dong")

if len(old_integrated) != 425:
    raise ValueError("Old Integrated khong du 425 dong")

if not new["OBJECTID"].is_unique:
    raise ValueError("OBJECTID moi bi trung")

if not mapping["OBJECTID_New"].is_unique:
    raise ValueError("OBJECTID_New bi trung")

if not mapping["OBJECTID_Old"].is_unique:
    raise ValueError("OBJECTID_Old bi trung")

if not old_integrated["OBJECTID"].is_unique:
    raise ValueError("OBJECTID cu bi trung")

if not mapping["_merge"].eq("both").all():
    raise ValueError("Mapping co su kien chua ghep")

# ==================================================
# 4. GHEP BANG ANH XA
# ==================================================

mapping_keys = mapping[
    ["OBJECTID_New", "OBJECTID_Old"]
].copy()

mapping_keys = mapping_keys.rename(
    columns={"OBJECTID_New": "OBJECTID"}
)

staging = new.merge(
    mapping_keys,
    on="OBJECTID",
    how="left",
    validate="one_to_one",
    indicator="_MappingStatus"
)

if not staging["_MappingStatus"].eq("both").all():
    raise ValueError("Co su kien moi chua co mapping")

staging = staging.drop(columns=["_MappingStatus"])

# ==================================================
# 5. LAY CAC THUOC TIN TICH HOP CU
# ==================================================

integration_columns = [
    "Water_ID",
    "DistanceToWater_m",
    "Population_Area_ID",
    "Population_Area_Name",
    "Population_ReferenceYear",
    "Population_BoundaryVersion",
    "Population_2019",
    "Population_Area_km2",
    "PopulationDensity_2019",
    "Population_Join_Status",
    "Nearest_Area_ID",
    "DistanceToNearestDistrict_m",
    "Population_Review_Note",
    "Nearest_Road_ID",
    "Nearest_Road_Name",
    "Nearest_Road_Mentioned_Years",
    "DistanceToNearestRoad_m",
    "Road_Distance_Band",
    "Road_Match_Status"
]

missing_columns = [
    col for col in integration_columns
    if col not in old_integrated.columns
]

if missing_columns:
    raise ValueError(
        "Thieu cot trong Old Integrated: "
        + str(missing_columns)
    )

old_features = old_integrated[
    ["OBJECTID"] + integration_columns
].copy()

old_features = old_features.rename(
    columns={"OBJECTID": "OBJECTID_Old"}
)

# ==================================================
# 6. GHEP THUOC TIN TICH HOP
# ==================================================

staging = staging.merge(
    old_features,
    on="OBJECTID_Old",
    how="left",
    validate="one_to_one",
    indicator="_IntegrationStatus"
)

if not staging["_IntegrationStatus"].eq("both").all():
    raise ValueError(
        "Co su kien chua ghep duoc du lieu tich hop"
    )

staging = staging.drop(columns=["_IntegrationStatus"])

# ==================================================
# 7. KIEM TRA KET QUA
# ==================================================

print("\n===== KIEM TRA KET QUA =====")

print("Tong dong:", len(staging))
print("Tong cot:", len(staging.columns))

print(
    "OBJECTID moi trung:",
    staging["OBJECTID"].duplicated().sum()
)

print(
    "OBJECTID cu trung:",
    staging["OBJECTID_Old"].duplicated().sum()
)

print(
    "Thieu DistanceToWater_m:",
    staging["DistanceToWater_m"].isna().sum()
)

print(
    "Thieu Population_Area_ID:",
    staging["Population_Area_ID"].isna().sum()
)

print(
    "Thieu Nearest_Road_ID:",
    staging["Nearest_Road_ID"].isna().sum()
)

print("\nTrang thai chat luong:")
print(
    staging["DataQualityStatus"].value_counts(
        dropna=False
    )
)

if len(staging) != 425:
    raise ValueError("So dong sau tich hop khong dung")

if staging["OBJECTID"].duplicated().any():
    raise ValueError("OBJECTID moi bi trung sau tich hop")

# ==================================================
# 8. XUAT FILE
# ==================================================

staging.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)

report_lines = [
    "INTEGRATED STAGING REPORT",
    "=========================",
    f"Rows: {len(staging)}",
    f"Columns: {len(staging.columns)}",
    f"Missing Water Distance: "
    f"{staging['DistanceToWater_m'].isna().sum()}",
    f"Missing Population Area: "
    f"{staging['Population_Area_ID'].isna().sum()}",
    f"Missing Nearest Road: "
    f"{staging['Nearest_Road_ID'].isna().sum()}",
    "",
    "Data Quality Status:",
    staging["DataQualityStatus"]
    .value_counts(dropna=False)
    .to_string()
]

report_file.write_text(
    "\n".join(report_lines),
    encoding="utf-8"
)

print("\n===== HOAN THANH TICH HOP =====")
print("Da luu:", output_file)
print("Bao cao:", report_file)


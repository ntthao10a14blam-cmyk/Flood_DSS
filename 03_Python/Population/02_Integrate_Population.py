
from pathlib import Path
import pandas as pd

BASE = Path(r"D:\Kho_du_lieu\Flood_DSS")

flood_path = BASE / "02_Staging_CSV/Integrated/Flood_With_Water.csv"
join_path = BASE / "02_Staging_CSV/Population/Flood_Population_Join.csv"
population_path = BASE / "02_Staging_CSV/Population/Population_Clean.csv"

output_path = BASE / "02_Staging_CSV/Integrated/Flood_Water_Population.csv"
log_path = BASE / "07_Logs/Population_Integration_Report.txt"

# 1. Đọc dữ liệu
flood = pd.read_csv(flood_path, encoding="utf-8-sig")
join = pd.read_csv(join_path, encoding="utf-8-sig")
population = pd.read_csv(population_path, encoding="utf-8-sig")

# 2. Kiểm tra cột bắt buộc
def require_columns(df, columns, name):
    missing = set(columns) - set(df.columns)
    if missing:
        raise ValueError(f"{name} thieu cot: {sorted(missing)}")

require_columns(flood, ["OBJECTID"], "Flood")
require_columns(join, ["OBJECTID", "D_Code"], "Spatial Join")
require_columns(
    population,
    ["Area_ID", "Area_Name", "Year",
     "BoundaryVersion", "Population",
     "Area_km2", "PopulationDensity"],
    "Population"
)

# 3. Kiểm tra khóa
assert flood["OBJECTID"].is_unique, "Flood OBJECTID bi trung"
assert join["OBJECTID"].is_unique, "Join OBJECTID bi trung"
assert population["Area_ID"].is_unique, "Population Area_ID bi trung"

assert flood["OBJECTID"].notna().all()
assert join["OBJECTID"].notna().all()
assert population["Area_ID"].notna().all()

# 4. Chuẩn hóa kiểu mã hành chính
join["D_Code"] = pd.to_numeric(join["D_Code"], errors="raise")
population["Area_ID"] = pd.to_numeric(
    population["Area_ID"], errors="raise"
)

# 5. Đổi tên mã hành chính trong bảng ánh xạ
join = join.rename(columns={"D_Code": "Population_Area_ID"})

# 6. Ghép Flood với bảng ánh xạ không gian
result = flood.merge(
    join,
    on="OBJECTID",
    how="left",
    validate="one_to_one",
    indicator="_spatial_merge"
)

if (result["_spatial_merge"] != "both").any():
    raise ValueError("Co OBJECTID Flood khong co trong bang Spatial Join")

result = result.drop(columns="_spatial_merge")

# 7. Chuẩn bị bảng Population
pop = population.rename(columns={
    "Area_ID": "Population_Area_ID",
    "Area_Name": "Population_Area_Name",
    "Year": "Population_ReferenceYear",
    "BoundaryVersion": "Population_BoundaryVersion",
    "Population": "Population_2019",
    "Area_km2": "Population_Area_km2",
    "PopulationDensity": "PopulationDensity_2019"
})

pop = pop[[
    "Population_Area_ID",
    "Population_Area_Name",
    "Population_ReferenceYear",
    "Population_BoundaryVersion",
    "Population_2019",
    "Population_Area_km2",
    "PopulationDensity_2019"
]]

# 8. Ghép dân số theo mã hành chính
result = result.merge(
    pop,
    on="Population_Area_ID",
    how="left",
    validate="many_to_one",
    indicator="_population_merge"
)

# 9. Phân loại trạng thái ghép
result["Population_Join_Status"] = "Matched_2019"

no_polygon = result["Population_Area_ID"].isna()
missing_population = (
    result["Population_Area_ID"].notna()
    & result["Population_2019"].isna()
)

result.loc[no_polygon, "Population_Join_Status"] = "Outside_2019_Polygon"
result.loc[missing_population, "Population_Join_Status"] = "Missing_Population_Data"

result = result.drop(columns="_population_merge")

# 10. Kiểm tra bảo toàn bản ghi
assert len(result) == len(flood), "So dong Flood bi thay doi"
assert result["OBJECTID"].is_unique, "OBJECTID bi trung sau merge"

# 11. Xuất kết quả
output_path.parent.mkdir(parents=True, exist_ok=True)
log_path.parent.mkdir(parents=True, exist_ok=True)

result.to_csv(output_path, index=False, encoding="utf-8-sig")

status = result["Population_Join_Status"].value_counts()

report = [
    "POPULATION INTEGRATION QUALITY REPORT",
    f"Flood input rows: {len(flood)}",
    f"Spatial Join rows: {len(join)}",
    f"Population rows: {len(population)}",
    f"Integrated rows: {len(result)}",
    f"Matched 2019: {int((result['Population_Join_Status'] == 'Matched_2019').sum())}",
    f"Outside 2019 polygon: {int(no_polygon.sum())}",
    f"Missing population data: {int(missing_population.sum())}",
    f"Unmatched OBJECTIDs: {result.loc[no_polygon, 'OBJECTID'].tolist()}",
    "Note: Population values refer to 2019, not the flood event year.",
    "Note: OBJECTID 184 requires separate spatial review.",
    f"Output: {output_path}"
]

log_path.write_text("\n".join(report), encoding="utf-8")

print("\n".join(report))
print("\nSTATUS COUNTS:")
print(status.to_string())


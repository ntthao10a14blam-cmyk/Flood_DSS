
from pathlib import Path
import pandas as pd

BASE = Path(r"D:\Kho_du_lieu\Flood_DSS")

input_file = BASE / "02_Staging_CSV/Population/Population_Raw.csv"
output_file = BASE / "02_Staging_CSV/Population/Population_Clean.csv"

df = pd.read_csv(input_file)

# Kiểm tra các cột bắt buộc
required = [
    "OBJECTID",
    "D_Code",
    "SUM_TongDans01",
    "SUM_Dientich_k",
    "Dens_district"
]

missing = set(required) - set(df.columns)
if missing:
    raise ValueError(f"Thieu cot: {missing}")

# Kiểm tra dữ liệu trước khi chuẩn hóa
assert len(df) == 24, "So dong khong dung 24"
assert df["D_Code"].is_unique, "D_Code bi trung"
assert df[required].notna().all().all(), "Co gia tri NULL"
assert (df["SUM_TongDans01"] >= 0).all()
assert (df["SUM_Dientich_k"] > 0).all()
assert (df["Dens_district"] >= 0).all()

calculated_density = (
    df["SUM_TongDans01"] / df["SUM_Dientich_k"]
)

assert (
    (calculated_density - df["Dens_district"]).abs() < 1
).all(), "Mat do dan so khong nhat quan"

# Chuẩn hóa tên thuộc tính
clean = df.rename(columns={
    "D_Code": "Area_ID",
    "SUM_TongDans01": "Population",
    "SUM_Dientich_k": "Area_km2",
    "Dens_district": "PopulationDensity"
}).copy()

# Chưa có bằng chứng để xác định các thông tin này

area_names = {
    760: "Quận 1",
    761: "Quận 12",
    762: "Quận Thủ Đức",
    763: "Quận 9",
    764: "Quận Gò Vấp",
    765: "Quận Bình Thạnh",
    766: "Quận Tân Bình",
    767: "Quận Tân Phú",
    768: "Quận Phú Nhuận",
    769: "Quận 2",
    770: "Quận 3",
    771: "Quận 10",
    772: "Quận 11",
    773: "Quận 4",
    774: "Quận 5",
    775: "Quận 6",
    776: "Quận 8",
    777: "Quận Bình Tân",
    778: "Quận 7",
    783: "Huyện Củ Chi",
    784: "Huyện Hóc Môn",
    785: "Huyện Bình Chánh",
    786: "Huyện Nhà Bè",
    787: "Huyện Cần Giờ"
}

clean["Area_Name"] = clean["Area_ID"].map(area_names)
clean["Year"] = 2019
clean["BoundaryVersion"] = "District_2019"

# Không cho phép thiếu tên hành chính
if clean["Area_Name"].isna().any():
    missing_codes = clean.loc[
        clean["Area_Name"].isna(), "Area_ID"
    ].tolist()
    raise ValueError(f"Ma hanh chinh chua doi chieu: {missing_codes}")

# Mã nhận diện nguồn nội bộ, không phải mã hành chính
clean["Source_ID"] = "POP_GPKG_01"

columns = [
    "OBJECTID",
    "Area_ID",
    "Area_Name",
    "Year",
    "BoundaryVersion",
    "Population",
    "Area_km2",
    "PopulationDensity",
    "Source_ID"
]

clean = clean[columns]

output_file.parent.mkdir(parents=True, exist_ok=True)
clean.to_csv(output_file, index=False, encoding="utf-8-sig")

print("=== POPULATION CLEANING ===")
print("Input rows:", len(df))
print("Output rows:", len(clean))
print("Duplicate Area_ID:", clean["Area_ID"].duplicated().sum())
print("Output:", output_file)
print("Year: 2019 (theo ten lop du lieu nguon)")
print("BoundaryVersion: District_2019 (nhan noi bo)")
print("Area_Name: Chua bo sung")
print("Can doi chieu phien ban dia gioi voi nguon chinh thuc.")

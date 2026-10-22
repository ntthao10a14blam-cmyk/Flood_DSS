
import pandas as pd
from pathlib import Path

base = Path(r"D:\Kho_du_lieu\Flood_DSS")

flood_path = base / "02_Staging_CSV" / "Flood_Clean.csv"
source_path = base / "01_Raw" / "Flood" / "Sources_floods_HCMC.tab"

flood = pd.read_csv(
    flood_path, encoding="utf-8-sig", dtype={"Source_id": "string"}
)

sources = pd.read_csv(
    source_path, sep="\t", encoding="utf-8-sig",
    dtype="string"
)

flood["Source_id"] = flood["Source_id"].str.strip()
sources["Source_id"] = sources["Source_id"].str.strip()

# 1. Tìm mã nguồn xuất hiện trong dữ liệu ngập
# nhưng không tồn tại trong bảng nguồn
missing_ids = sorted(
    set(flood["Source_id"].dropna())
    - set(sources["Source_id"].dropna())
)

print("=== MA NGUON KHONG CO TRONG BANG NGUON ===")
print(missing_ids)

# 2. Đếm số bản ghi ngập bị ảnh hưởng
affected = flood[flood["Source_id"].isin(missing_ids)]

print("\n=== SO BAN GHI BI ANH HUONG ===")
print(len(affected))

print("\n=== SO LUONG THEO MA NGUON ===")
print(affected["Source_id"].value_counts().to_string())

# 3. Kiểm tra các mã nguồn trùng
duplicate_sources = sources[
    sources["Source_id"].duplicated(keep=False)
]

print("\n=== CAC MA NGUON TRUNG ===")
print(duplicate_sources.to_string(index=False))

# 4. Xuất danh sách để kiểm tra
report_path = base / "07_Logs" / "Missing_Source_Records.csv"

affected.to_csv(
    report_path, index=False, encoding="utf-8-sig"
)

print("\nFile bao cao:", report_path)


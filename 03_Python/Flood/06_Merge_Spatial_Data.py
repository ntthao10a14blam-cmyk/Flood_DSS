
import pandas as pd
from pathlib import Path

base = Path(r"D:\Kho_du_lieu\Flood_DSS")
folder = base / "02_Staging_CSV"

clean = pd.read_csv(
    folder / "Flood_Clean.csv",
    encoding="utf-8-sig"
)

spatial = pd.read_csv(
    folder / "Flood_With_Province.csv",
    encoding="utf-8-sig"
)

# Kiểm tra khóa OBJECTID
for name, df in [("Clean", clean), ("Spatial", spatial)]:
    if df["OBJECTID"].isna().any():
        raise ValueError(f"{name}: OBJECTID bi thieu")
    if df["OBJECTID"].duplicated().any():
        raise ValueError(f"{name}: OBJECTID bi trung")

# Chỉ lấy cột địa giới từ Spatial Join
province = spatial[["OBJECTID", "GhiChu"]].copy()
province = province.rename(
    columns={"GhiChu": "Province_Joined"}
)

# Ghép theo OBJECTID của cùng nguồn GIS
result = clean.merge(
    province,
    on="OBJECTID",
    how="left",
    validate="one_to_one",
    indicator=True
)

if len(result) != 425:
    raise ValueError("So ban ghi sau khi ghep khong dung 425")

if (result["_merge"] != "both").any():
    raise ValueError("Co OBJECTID khong khop giua hai file")

result = result.drop(columns=["_merge"])

# Lưu cả vùng ghi nhận gốc và vùng ghép không gian
# Province: thuộc tính gốc
# Province_Joined: kết quả Spatial Join

output = folder / "Flood_Staging_Final.csv"

result.to_csv(
    output,
    index=False,
    encoding="utf-8-sig"
)

print("=== KET QUA MERGE SPATIAL ===")
print("Tong ban ghi:", len(result))
print("\nThong ke vung:")
print(result["Province_Joined"].value_counts(dropna=False))
print("\nFile:", output)


import pandas as pd
from pathlib import Path

# Thay bằng đường dẫn thật tìm được ở Bước 3
file_path = Path(
    r"D:\Kho_du_lieu\Flood_DSS\01_Raw\Flood\Flood_event_locations.tab"
)

df = pd.read_csv(
    file_path,
    sep="\t",
    encoding="utf-8-sig",
    dtype="string"
)

print("TỔNG SỐ DÒNG:", len(df))
print("TỔNG SỐ CỘT:", len(df.columns))

print("\nDANH SÁCH CỘT:")
print(df.columns.tolist())

print("\nDỮ LIỆU THIẾU:")
print(df.isna().sum())

print("\nKIỂM TRA TRÙNG Obs_id:")
print(df[df["Obs_id"].duplicated(keep=False)])

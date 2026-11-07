
import pandas as pd

from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
file_path = ROOT / "02_Staging_CSV" / "Flood" / "Flood_GIS_Raw.csv"

df = pd.read_csv(file_path, encoding="utf-8-sig")

print("=== KIEM TRA DU LIEU NGAP ===")

print("\n1. Tong so ban ghi:")
print(len(df))

print("\n2. Danh sach cot:")
for col in df.columns:
    print("-", col)

print("\n3. So gia tri thieu theo cot:")
print(df.isna().sum().to_string())

print("\n4. Kiem tra Obs_id trung:")
if "Obs_id" in df.columns:
    print(df[df.duplicated("Obs_id", keep=False)])
else:
    print("Khong tim thay cot Obs_id")

print("\n5. Nam dong dau tien:")
print(df.head().to_string())

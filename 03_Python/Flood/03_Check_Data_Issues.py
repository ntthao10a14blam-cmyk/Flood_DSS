
import pandas as pd
from pathlib import Path

base = Path(r"D:\Kho_du_lieu\Flood_DSS")

file = base / "02_Staging_CSV" / "Flood_Clean.csv"

df = pd.read_csv(file, encoding="utf-8-sig")

# Kiểm tra bản ghi có ngày và năm không khớp
issues = df[df["Year_Date_Mismatch"] == True]

columns = [
    "OBJECTID",
    "Obs_id",
    "Date",
    "Year",
    "Location_name",
    "Source_id",
    "Observation_notes"
]

print("=== BAN GHI CO NAM VA NGAY KHONG KHOP ===")
print(issues[columns].to_string(index=False))

# Kiểm tra bản ghi trùng Obs_id
duplicates = df[df["Duplicate_Obs_id"] == True]

print("\n=== BAN GHI TRUNG OBS_ID ===")
print(
    duplicates[
        ["OBJECTID", "Obs_id", "Year", "Location_name"]
    ].to_string(index=False)
)


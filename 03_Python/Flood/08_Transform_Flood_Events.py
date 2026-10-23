
from pathlib import Path
import pandas as pd

# ===== 1. ĐƯỜNG DẪN =====
ROOT = Path(r"D:\Kho_du_lieu\Flood_DSS")

INPUT = ROOT / "01_Raw/Flood/Flood_event_locations.tab"
OUTPUT = ROOT / "02_Staging_CSV/Flood"
LOG = ROOT / "07_Logs"

OUTPUT.mkdir(parents=True, exist_ok=True)
LOG.mkdir(parents=True, exist_ok=True)

# ===== 2. ĐỌC FILE GỐC =====
df = pd.read_csv(
    INPUT,
    sep="\t",
    encoding="utf-8-sig",
    dtype="string",
    keep_default_na=False
)

original_rows = len(df)
df.columns = df.columns.str.strip()

# ===== 3. KIỂM TRA CỘT =====
expected = [
    "OBJECTID", "Obs_id", "Date", "Year",
    "Location name", "Location type",
    "District mentioned", "Province",
    "Ward/Phường", "Commune/Xã",
    "Current admin unit",
    "Water height min (cm)",
    "Water height max (cm)",
    "Depth class", "Cause", "Impact type",
    "Source id", "Source type",
    "Spatial precision", "Geocoding method",
    "Duration (h)", "Observation notes"
]

missing = [c for c in expected if c not in df.columns]

if missing:
    raise ValueError(f"Thiếu cột: {missing}")

# ===== 4. ĐỔI TÊN CỘT =====
rename = {
    "Obs_id": "Obs_ID",
    "Location name": "Location_Name",
    "Location type": "Location_Type",
    "District mentioned": "District_Mentioned",
    "Ward/Phường": "Ward",
    "Commune/Xã": "Commune",
    "Current admin unit": "Current_Admin_Unit",
    "Water height min (cm)": "MinDepth_cm",
    "Water height max (cm)": "MaxDepth_cm",
    "Depth class": "Depth_Class",
    "Impact type": "Impact_Type",
    "Source id": "Source_ID",
    "Source type": "Source_Type",
    "Spatial precision": "Spatial_Precision",
    "Geocoding method": "Geocoding_Method",
    "Duration (h)": "Duration_hours",
    "Observation notes": "Observation_Notes"
}

df = df.rename(columns=rename)

# ===== 5. CHUẨN HÓA KHOẢNG TRẮNG =====
for col in df.columns:
    df[col] = df[col].str.strip()
    df[col] = df[col].replace("", pd.NA)

# ===== 6. CHUẨN HÓA SỐ =====
invalid_numeric = pd.Series(False, index=df.index)

numeric_columns = [
    "OBJECTID", "Year",
    "MinDepth_cm", "MaxDepth_cm",
    "Duration_hours"
]

for col in numeric_columns:
    raw = df[col]
    normalized = raw.str.replace(
        ",", ".", regex=False
    )
    converted = pd.to_numeric(
        normalized, errors="coerce"
    )

    invalid_numeric |= raw.notna() & converted.isna()
    df[col] = converted

# ===== 7. CHUẨN HÓA NGÀY =====
raw_date = df["Date"].copy()

parsed_date = pd.to_datetime(
    raw_date,
    format="%d/%m/%Y",
    errors="coerce"
)

invalid_date = raw_date.notna() & parsed_date.isna()

df["Date"] = parsed_date

# ===== 8. CHUẨN HÓA NHÃN =====
df["Spatial_Precision"] = (
    df["Spatial_Precision"]
    .replace({
        "Hgh": "High",
        "Hugh": "High"
    })
)

# ===== 9. KIỂM TRA TRÙNG =====
df["DuplicateOBJECTID"] = (
    df["OBJECTID"].notna()
    & df["OBJECTID"].duplicated(keep=False)
)

df["DuplicateObsID"] = (
    df["Obs_ID"].notna()
    & df["Obs_ID"].duplicated(keep=False)
)

# ===== 10. KIỂM TRA NGÀY / NĂM =====
df["DateYearMismatch"] = (
    df["Date"].notna()
    & df["Year"].notna()
    & (df["Date"].dt.year != df["Year"])
)

# ===== 11. KIỂM TRA ĐỘ SÂU =====
df["InvalidDepthRange"] = (
    df["MinDepth_cm"].notna()
    & df["MaxDepth_cm"].notna()
    & (df["MinDepth_cm"] > df["MaxDepth_cm"])
)

df["NegativeDepth"] = (
    df["MinDepth_cm"].lt(0).fillna(False)
    | df["MaxDepth_cm"].lt(0).fillna(False)
)

df["NegativeDuration"] = (
    df["Duration_hours"].lt(0).fillna(False)
)

# ===== 12. GẮN CỜ CHẤT LƯỢNG =====
df["InvalidNumeric"] = invalid_numeric
df["InvalidDate"] = invalid_date

flags = [
    "DuplicateOBJECTID",
    "DuplicateObsID",
    "DateYearMismatch",
    "InvalidDepthRange",
    "NegativeDepth",
    "NegativeDuration",
    "InvalidNumeric",
    "InvalidDate"
]

has_issue = df[flags].any(axis=1)

df["DataQualityStatus"] = "Valid"
df.loc[has_issue, "DataQualityStatus"] = "Review"

# ===== 13. CHUẨN HÓA NGÀY XUẤT CSV =====
df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")

# ===== 14. XUẤT FILE =====
clean_file = OUTPUT / "Flood_Events_Clean.csv"
issues_file = OUTPUT / "Flood_Events_Issues.csv"

df.to_csv(
    clean_file,
    index=False,
    encoding="utf-8-sig"
)

df.loc[has_issue].to_csv(
    issues_file,
    index=False,
    encoding="utf-8-sig"
)

# ===== 15. BÁO CÁO =====
report = [
    "FLOOD EVENT CLEANING REPORT",
    f"Original rows: {original_rows}",
    f"Output rows: {len(df)}",
    f"Review rows: {int(has_issue.sum())}",
    "",
    "ISSUE COUNTS:"
]

for flag in flags:
    report.append(f"{flag}: {int(df[flag].sum())}")

report += [
    "",
    "MISSING VALUES:",
    df.isna().sum().to_string()
]

report_file = LOG / "Flood_Events_Cleaning_Report.txt"
report_file.write_text(
    "\n".join(report),
    encoding="utf-8"
)

print("\n===== HOAN THANH =====")
print("So dong goc:", original_rows)
print("So dong sau lam sach:", len(df))
print("So dong can xem lai:", int(has_issue.sum()))
print("File clean:", clean_file)
print("File issues:", issues_file)
print("Bao cao:", report_file)

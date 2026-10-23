
from pathlib import Path
import pandas as pd
import unicodedata
import re

# ==================================================
# 1. KHAI BAO DUONG DAN
# ==================================================

ROOT = Path(r"D:\Kho_du_lieu\Flood_DSS")
FOLDER = ROOT / "02_Staging_CSV" / "Flood"

clean_file = FOLDER / "Flood_Events_Clean.csv"
spatial_file = FOLDER / "Flood_Events_Spatial.csv"
output_file = FOLDER / "Flood_Events_Staging.csv"


# ==================================================
# 2. DOC DU LIEU
# ==================================================

clean = pd.read_csv(clean_file, dtype="string")
spatial = pd.read_csv(spatial_file, dtype="string")

print("===== KIEM TRA DU LIEU =====")
print("Clean:", len(clean))
print("Spatial:", len(spatial))

if len(clean) != len(spatial):
    raise ValueError("Hai file khong cung so dong")

# Reset index de doi chieu theo vi tri dong
clean = clean.reset_index(drop=True)
spatial = spatial.reset_index(drop=True)


# ==================================================
# 3. HAM CHUAN HOA CHUOI
# ==================================================

def normalize_text(series):
    def normalize(value):
        if pd.isna(value):
            return ""

        value = unicodedata.normalize("NFC", str(value))
        value = re.sub(r"\s+", " ", value.strip())

        return value.casefold()

    return series.map(normalize)


# ==================================================
# 4. KIEM TRA SU TUONG UNG GIUA HAI FILE
# ==================================================

checks = {
    "Obs_ID": (
        normalize_text(clean["Obs_ID"])
        == normalize_text(spatial["Obs_id"])
    ),
    "Year": (
        normalize_text(clean["Year"])
        == normalize_text(spatial["Year"])
    ),
    "Location": (
        normalize_text(clean["Location_Name"])
        == normalize_text(spatial["Location_name"])
    )
}

all_match = pd.Series(True, index=clean.index)

for name, result in checks.items():
    print(
        f"{name} khop:",
        int(result.sum()),
        "/",
        len(result)
    )

    all_match &= result

if not all_match.all():
    print("\n===== CAC DONG KHONG KHOP =====")

    positions = clean.index[~all_match]

    for i in positions[:20]:
        print(
            "Dong:", i + 1,
            "| Clean:",
            clean.loc[i, "Obs_ID"],
            clean.loc[i, "Year"],
            clean.loc[i, "Location_Name"],
            "| Spatial:",
            spatial.loc[i, "Obs_id"],
            spatial.loc[i, "Year"],
            spatial.loc[i, "Location_name"]
        )

    raise ValueError(
        "Du lieu khong tuong ung. "
        "Khong duoc ghep toa do theo thu tu."
    )


# ==================================================
# 5. GHEP TOA DO TU GIS VAO DU LIEU CLEAN
# ==================================================

staging = clean.copy()

staging["Longitude"] = pd.to_numeric(
    spatial["Longitude"],
    errors="coerce"
)

staging["Latitude"] = pd.to_numeric(
    spatial["Latitude"],
    errors="coerce"
)


# ==================================================
# 6. KIEM TRA TOA DO
# ==================================================

missing_coords = staging[
    ["Longitude", "Latitude"]
].isna().any(axis=1)

invalid_coords = (
    ~staging["Longitude"].between(-180, 180)
    | ~staging["Latitude"].between(-90, 90)
)

print("\n===== KIEM TRA TOA DO =====")
print("Thieu toa do:", int(missing_coords.sum()))
print("Toa do khong hop le:", int(invalid_coords.sum()))

if missing_coords.any() or invalid_coords.any():
    raise ValueError(
        "Toa do bi thieu hoac khong hop le"
    )


# ==================================================
# 7. KIEM TRA KHOA OBJECTID
# ==================================================

if staging["OBJECTID"].isna().any():
    raise ValueError("OBJECTID cua Clean bi thieu")

if staging["OBJECTID"].duplicated().any():
    raise ValueError("OBJECTID cua Clean bi trung")


# ==================================================
# 8. SAP XEP CAC COT DU LIEU
# ==================================================

base_columns = [
    "OBJECTID",
    "Obs_ID",
    "Date",
    "Year",
    "Location_Name",
    "Location_Type",
    "District_Mentioned",
    "Province",
    "Ward",
    "Commune",
    "Current_Admin_Unit",
    "MinDepth_cm",
    "MaxDepth_cm",
    "Depth_Class",
    "Cause",
    "Impact_Type",
    "Source_ID",
    "Source_Type",
    "Spatial_Precision",
    "Geocoding_Method",
    "Duration_hours",
    "Observation_Notes",
    "Longitude",
    "Latitude"
]

# Giu lai cac cot kiem tra chat luong du lieu
quality_columns = [
    col for col in staging.columns
    if col not in base_columns
]

staging = staging[
    base_columns + quality_columns
]


# ==================================================
# 9. XUAT FILE STAGING CSV
# ==================================================

staging.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)


# ==================================================
# 10. BAO CAO KET QUA
# ==================================================

print("\n===== HOAN THANH FLOOD STAGING =====")

print("Tong dong:", len(staging))
print("Tong cot:", len(staging.columns))

print(
    "OBJECTID trung:",
    staging["OBJECTID"].duplicated().sum()
)

print("\nTrang thai chat luong:")

print(
    staging["DataQualityStatus"].value_counts(
        dropna=False
    )
)

print("\nDa luu file:")
print(output_file)

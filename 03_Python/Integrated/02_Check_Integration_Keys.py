
from pathlib import Path
import pandas as pd
import unicodedata
import re

ROOT = Path(r"D:\Kho_du_lieu\Flood_DSS")
BASE = ROOT / "02_Staging_CSV"
LOGS = ROOT / "07_Logs"

LOGS.mkdir(parents=True, exist_ok=True)

new = pd.read_csv(
    BASE / "Flood/Flood_Events_Staging.csv",
    dtype="string"
)

old = pd.read_csv(
    BASE / "Flood/Flood_Staging_Final.csv",
    dtype="string"
)

water = pd.read_csv(
    BASE / "Water/Flood_Water_Distance.csv",
    dtype="string"
)

population = pd.read_csv(
    BASE / "Population/Flood_Population_Join.csv",
    dtype="string"
)

integrated = pd.read_csv(
    BASE / "Integrated/Flood_Water_Population_Roads.csv",
    dtype="string"
)


def normalize(value):
    if pd.isna(value):
        return ""

    value = unicodedata.normalize("NFC", str(value))
    value = re.sub(r"\s+", " ", value.strip())

    return value.casefold()


def make_event_key(df, id_col, year_col, location_col):
    return (
        df[id_col].map(normalize)
        + "|"
        + df[year_col].map(normalize)
        + "|"
        + df[location_col].map(normalize)
    )


print("===== KIEM TRA KHOA SU KIEN =====")

new["EventKey"] = make_event_key(
    new, "Obs_ID", "Year", "Location_Name"
)

old["EventKey"] = make_event_key(
    old, "Obs_id", "Year", "Location_name"
)

integrated["EventKey"] = make_event_key(
    integrated, "Obs_id", "Year", "Location_name"
)

for name, df in [
    ("Flood_New", new),
    ("Flood_Old", old),
    ("Flood_Integrated", integrated)
]:
    print(f"\n{name}")
    print("So dong:", len(df))
    print(
        "EventKey trung:",
        int(df["EventKey"].duplicated().sum())
    )
    print(
        "OBJECTID trung:",
        int(df["OBJECTID"].duplicated().sum())
    )


# ==============================================
# SO SANH OBJECTID CUA HAI PHIEN BAN
# ==============================================

mapping = new[
    ["OBJECTID", "EventKey", "Obs_ID", "Year", "Location_Name"]
].merge(
    old[
        ["OBJECTID", "EventKey"]
    ],
    on="EventKey",
    how="outer",
    suffixes=("_New", "_Old"),
    indicator=True,
    validate="one_to_one"
)

mapping["OBJECTID_Match"] = (
    mapping["OBJECTID_New"]
    == mapping["OBJECTID_Old"]
)

print("\n===== SO SANH OBJECTID =====")
print("Tong dong mapping:", len(mapping))
print("\nTrang thai ghep:")
print(mapping["_merge"].value_counts())

matched = mapping[mapping["_merge"] == "both"]

print(
    "OBJECTID giong nhau:",
    int(matched["OBJECTID_Match"].sum())
)

print(
    "OBJECTID khac nhau:",
    int((~matched["OBJECTID_Match"]).sum())
)


# ==============================================
# KIEM TRA OBJECTID TRONG FILE TICH HOP
# ==============================================

print("\n===== KIEM TRA FILE TICH HOP =====")

old_ids = set(old["OBJECTID"].dropna())
new_ids = set(new["OBJECTID"].dropna())

for name, df in [
    ("Water_Distance", water),
    ("Flood_Population", population),
    ("Flood_Integrated", integrated)
]:
    ids = set(df["OBJECTID"].dropna())

    print(f"\n{name}")
    print("So dong:", len(df))
    print("OBJECTID duy nhat:", len(ids))
    print("Ma thuoc Flood_Old:", len(ids & old_ids))
    print("Ma thuoc Flood_New:", len(ids & new_ids))


# ==============================================
# KIEM TRA LIEN KET THEO EVENTKEY
# ==============================================

comparison = integrated[
    ["OBJECTID", "EventKey"]
].merge(
    old[["OBJECTID", "EventKey"]],
    on="EventKey",
    how="outer",
    suffixes=("_Integrated", "_Old"),
    indicator=True,
    validate="one_to_one"
)

both = comparison[comparison["_merge"] == "both"]

print("\n===== INTEGRATED VS FLOOD OLD =====")
print(comparison["_merge"].value_counts())

print(
    "OBJECTID khop theo EventKey:",
    int(
        (
            both["OBJECTID_Integrated"]
            == both["OBJECTID_Old"]
        ).sum()
    )
)


# ==============================================
# XUAT BAO CAO
# ==============================================

mapping.to_csv(
    LOGS / "Flood_Old_New_ID_Mapping.csv",
    index=False,
    encoding="utf-8-sig"
)

comparison.to_csv(
    LOGS / "Flood_Integrated_Key_Check.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\n===== HOAN THANH =====")
print("Da xuat:")
print("Flood_Old_New_ID_Mapping.csv")
print("Flood_Integrated_Key_Check.csv")

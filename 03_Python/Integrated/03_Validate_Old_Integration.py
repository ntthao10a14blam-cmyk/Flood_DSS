
from pathlib import Path
import pandas as pd

ROOT = Path(r"D:\Kho_du_lieu\Flood_DSS")
STAGING = ROOT / "02_Staging_CSV"
LOGS = ROOT / "07_Logs"

mapping = pd.read_csv(
    LOGS / "Flood_Old_New_ID_Mapping.csv",
    dtype="string"
)

FILES = {
    "Water_Distance": STAGING / "Water/Flood_Water_Distance.csv",
    "Flood_Population": STAGING / "Population/Flood_Population_Join.csv",
    "Flood_Integrated": STAGING / "Integrated/Flood_Water_Population_Roads.csv"
}

print("===== KIEM TRA BANG ANH XA =====")

assert len(mapping) == 425
assert mapping["OBJECTID_New"].is_unique
assert mapping["OBJECTID_Old"].is_unique
assert mapping["_merge"].eq("both").all()

old_ids = set(mapping["OBJECTID_Old"])

results = []

for name, path in FILES.items():

    df = pd.read_csv(path, dtype="string")

    ids = set(df["OBJECTID"].dropna())

    duplicate_ids = int(
        df["OBJECTID"].duplicated().sum()
    )

    missing_ids = old_ids - ids
    extra_ids = ids - old_ids

    status = (
        "PASS"
        if len(df) == 425
        and duplicate_ids == 0
        and not missing_ids
        and not extra_ids
        else "REVIEW"
    )

    print(f"\n===== {name} =====")
    print("So dong:", len(df))
    print("OBJECTID trung:", duplicate_ids)
    print("Thieu OBJECTID cu:", len(missing_ids))
    print("OBJECTID ngoai mapping:", len(extra_ids))
    print("Ket qua:", status)

    results.append({
        "Dataset": name,
        "Rows": len(df),
        "DuplicateOBJECTID": duplicate_ids,
        "MissingOldIDs": len(missing_ids),
        "ExtraIDs": len(extra_ids),
        "Status": status
    })

report = pd.DataFrame(results)

output = LOGS / "Old_Integration_Validation.csv"

report.to_csv(
    output,
    index=False,
    encoding="utf-8-sig"
)

print("\n===== TONG KET =====")
print(report.to_string(index=False))
print("\nDa luu:", output)


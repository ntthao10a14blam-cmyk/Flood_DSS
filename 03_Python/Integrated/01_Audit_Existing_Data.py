
from pathlib import Path
import pandas as pd

ROOT = Path(r"D:\Kho_du_lieu\Flood_DSS")

FILES = {
    "Flood_New": "02_Staging_CSV/Flood/Flood_Events_Staging.csv",
    "Flood_Old": "02_Staging_CSV/Flood/Flood_Staging_Final.csv",
    "Population": "02_Staging_CSV/Population/Population_Clean.csv",
    "Roads": "02_Staging_CSV/Roads/Roads_Clean.csv",
    "Water_Distance": "02_Staging_CSV/Water/Flood_Water_Distance.csv",
    "Flood_Population": "02_Staging_CSV/Population/Flood_Population_Join.csv",
    "Flood_Integrated": "02_Staging_CSV/Integrated/Flood_Water_Population_Roads.csv"
}

REPORT_DIR = ROOT / "07_Logs"
REPORT_DIR.mkdir(parents=True, exist_ok=True)

summary = []
columns_report = []
datasets = {}

print("===== KIEM TRA DU LIEU DA LAM SACH =====")

for name, relative_path in FILES.items():

    path = ROOT / relative_path

    if not path.exists():
        print(f"\n{name}: KHONG TIM THAY FILE")
        summary.append({
            "Dataset": name,
            "File": relative_path,
            "Status": "Missing"
        })
        continue

    try:
        df = pd.read_csv(
            path,
            dtype="string",
            encoding="utf-8-sig",
            low_memory=False
        )

        datasets[name] = df

        missing_cells = int(df.isna().sum().sum())
        duplicate_rows = int(df.duplicated().sum())

        summary.append({
            "Dataset": name,
            "File": relative_path,
            "Status": "Found",
            "Rows": len(df),
            "Columns": len(df.columns),
            "MissingCells": missing_cells,
            "DuplicateRows": duplicate_rows
        })

        print(f"\n===== {name} =====")
        print("So dong:", len(df))
        print("So cot:", len(df.columns))
        print("O thieu:", missing_cells)
        print("Dong trung hoan toan:", duplicate_rows)

        print("Danh sach cot:")
        for col in df.columns:
            print(" -", col)

            columns_report.append({
                "Dataset": name,
                "Column": col,
                "MissingCount": int(df[col].isna().sum()),
                "MissingPercent": round(
                    df[col].isna().mean() * 100, 2
                )
            })

    except Exception as error:
        print(f"\n{name}: LOI DOC FILE")
        print(error)

        summary.append({
            "Dataset": name,
            "File": relative_path,
            "Status": "ReadError",
            "Error": str(error)
        })


# ==============================================
# DOI CHIEU MA SU KIEN NGAP
# ==============================================

print("\n===== DOI CHIEU DU LIEU NGAP =====")

if "Flood_New" in datasets:

    new_df = datasets["Flood_New"]

    print("Flood_New:", len(new_df), "dong")

    for name in ["Flood_Old", "Flood_Population",
                 "Water_Distance", "Flood_Integrated"]:

        if name not in datasets:
            continue

        df = datasets[name]

        print(f"\n{name}: {len(df)} dong")

        possible_ids = [
            "Obs_ID", "Obs_id", "Flood_ID",
            "FloodID", "OBJECTID"
        ]

        available = [
            col for col in possible_ids
            if col in df.columns
        ]

        print("Cot dinh danh tim thay:", available)

        if "Obs_ID" in new_df.columns:
            new_ids = set(
                new_df["Obs_ID"].dropna().astype(str)
            )

            for col in ["Obs_ID", "Obs_id"]:
                if col in df.columns:
                    old_ids = set(
                        df[col].dropna().astype(str)
                    )

                    print(
                        f"Ma trung theo {col}:",
                        len(new_ids & old_ids)
                    )
                    print(
                        "Ma chi co trong file moi:",
                        len(new_ids - old_ids)
                    )
                    print(
                        "Ma chi co trong file cu:",
                        len(old_ids - new_ids)
                    )


# ==============================================
# XUAT BAO CAO
# ==============================================

summary_file = REPORT_DIR / "Data_Audit_Summary.csv"
columns_file = REPORT_DIR / "Data_Audit_Columns.csv"

pd.DataFrame(summary).to_csv(
    summary_file,
    index=False,
    encoding="utf-8-sig"
)

pd.DataFrame(columns_report).to_csv(
    columns_file,
    index=False,
    encoding="utf-8-sig"
)

print("\n===== HOAN THANH KIEM TRA =====")
print("Bao cao tong hop:", summary_file)
print("Bao cao cot:", columns_file)


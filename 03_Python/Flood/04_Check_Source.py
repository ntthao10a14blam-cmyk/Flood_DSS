
import pandas as pd

path = r"D:\Kho_du_lieu\Flood_DSS\01_Raw\Flood\Sources_floods_HCMC.tab"

df = pd.read_csv(
    path,
    sep="\t",
    dtype=str,
    encoding="utf-8-sig"
)

df.columns = df.columns.str.strip()
df["Source_id"] = df["Source_id"].str.strip()

print("=== TONG SO NGUON ===")
print(len(df))

print("\n=== DANH SACH MA NGUON ===")
print(df["Source_id"].to_string(index=False))

print("\n=== TIM SRC_38 ===")
print(df[df["Source_id"] == "SRC_38"].to_string(index=False))

print("\n=== CAC MA NGUON GAN SRC_38 ===")
print(
    df[df["Source_id"].str.contains(
        r"SRC_3[5-9]|SRC_4[0-2]",
        na=False,
        regex=True
    )].to_string(index=False)
)

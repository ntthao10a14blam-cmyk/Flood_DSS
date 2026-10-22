from pathlib import Path
import pandas as pd

ROOT = Path(r'D:\Kho_du_lieu\Flood_DSS')
WATER = ROOT / '02_Staging_CSV' / 'Water' / 'Flood_Water_Distance.csv'
FLOOD = ROOT / '02_Staging_CSV' / 'Flood' / 'Flood_Staging_Final.csv'
OUTPUT = ROOT / '02_Staging_CSV' / 'Integrated' / 'Flood_With_Water.csv'
LOG = ROOT / '07_Logs' / 'Water_Distance_Quality_Report.txt'

water = pd.read_csv(WATER, encoding='utf-8-sig')
flood = pd.read_csv(FLOOD, encoding='utf-8-sig')
required = {'OBJECTID', 'Water_ID', 'DistanceToWater_m'}
assert required.issubset(water.columns), f'Missing Water fields: {required - set(water.columns)}'
assert 'OBJECTID' in flood.columns, 'Missing Flood OBJECTID'
assert len(water) == 425 and len(flood) == 425, 'Unexpected number of rows'
assert water['OBJECTID'].notna().all() and flood['OBJECTID'].notna().all()
assert water['OBJECTID'].is_unique and flood['OBJECTID'].is_unique
assert water[list(required)].notna().all().all(), 'Missing values in Water data'
assert pd.api.types.is_numeric_dtype(water['DistanceToWater_m'])
assert (water['DistanceToWater_m'] >= 0).all(), 'Negative distance detected'
assert set(flood['OBJECTID']) == set(water['OBJECTID']), 'Flood/Water OBJECTID mismatch'

merged = flood.merge(water[['OBJECTID','Water_ID','DistanceToWater_m']], on='OBJECTID', how='left', validate='one_to_one', indicator=True)
assert len(merged) == len(flood) and merged['_merge'].eq('both').all()
merged = merged.drop(columns=['_merge'])
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
LOG.parent.mkdir(parents=True, exist_ok=True)
merged.to_csv(OUTPUT, index=False, encoding='utf-8-sig')
report = f'''WATER DISTANCE ETL QUALITY REPORT\nWater rows: {len(water)}\nFlood rows: {len(flood)}\nIntegrated rows: {len(merged)}\nWater missing distances: {water['DistanceToWater_m'].isna().sum()}\nWater negative distances: {(water['DistanceToWater_m'] < 0).sum()}\nDistance min (m): {water['DistanceToWater_m'].min():.6f}\nDistance mean (m): {water['DistanceToWater_m'].mean():.6f}\nDistance max (m): {water['DistanceToWater_m'].max():.6f}\nDistinct nearest Water IDs: {water['Water_ID'].nunique()}\nOutput: {OUTPUT}\nNote: Large distances may reflect Water layer coverage; do not delete automatically.\n'''
LOG.write_text(report, encoding='utf-8')
print(report)

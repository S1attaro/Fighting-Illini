import hashlib
from pathlib import Path

files = [
    "SIPRI-Milex-data-2017-2025.xlsx",
    "API_MS.MIL.XPND.GD.ZS_DS2_en_csv_v2_211.csv",
    "Europe-Central-Asia_aggregated_data_up_to_week_of-2026-03-28.xlsx"
]

for filename in files:
    path = Path(filename)
    if path.exists():
        sha256 = hashlib.sha256(path.read_bytes()).hexdigest()
        print(f"{filename}")
        print(f"  sha256: {sha256}")
    else:
        print(f"{filename} - FILE NOT FOUND")
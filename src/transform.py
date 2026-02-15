# Import modules
import os
from pathlib import Path
import pandas as pd
import numpy as np
import sqlite3

# Paths
script_dir = Path(__file__).resolve().parent
db_path = script_dir.parent / "db" / "energy.sqlite"
out_path = script_dir.parent / "data" / "final_df.parquet"

if not db_path.exists():
    raise FileNotFoundError(f"Database not found at {db_path}")

# Load SQL master table into python
conn = sqlite3.connect(str(db_path))
try:
    df = pd.read_sql_query("SELECT * FROM master WHERE year >= 1950 AND year < 2024;", conn)
finally:
    conn.close()

# Safely coerce string columns if they exist
for c in ("country", "iso_code"):
    if c in df.columns:
        df[c] = df[c].astype(str)

# Coerce year safely
if "year" in df.columns:
    df["year"] = pd.to_numeric(df["year"], errors="coerce").astype("Int64")

# Columns to normalize (only operate on those that exist)
cols = [
    "renewables_share_energy","fossil_share_energy","co2_per_capita",
    "primary_energy_consumption","energy_per_capita","electricity_demand","gdp_per_capita",
    "solar_share_elec","wind_share_elec","co2"
]
existing = [c for c in cols if c in df.columns]
if existing:
    # Replace empty-string cells with NaN, then coerce to numeric
    df[existing] = df[existing].replace(r"^\s*$", np.nan, regex=True)
    df[existing] = df[existing].apply(pd.to_numeric, errors="coerce")

# Ensure output directory exists and write parquet
out_path.parent.mkdir(parents=True, exist_ok=True)
df.to_parquet(out_path, index=False)

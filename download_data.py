import os
import pandas as pd
from urllib.request import Request, urlopen

os.makedirs("data/raw", exist_ok=True)

energy_url = "https://owid-public.owid.io/data/energy/owid-energy-data.csv"
co2_url = "https://owid-public.owid.io/data/co2/owid-co2-data.csv"
gdp_url = "https://ourworldindata.org/grapher/gdp-per-capita-worldbank.csv"

def read_csv_with_user_agent(url: str) -> pd.DataFrame:
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req) as resp:
        return pd.read_csv(resp)

read_csv_with_user_agent(energy_url).to_csv("data/raw/owid-energy-data.csv", index=False)
read_csv_with_user_agent(co2_url).to_csv("data/raw/owid-co2-data.csv", index=False)

pd.read_csv(gdp_url).to_csv("data/raw/gdp-per-capita-worldbank.csv", index=False)

print("Raw data downloaded.")

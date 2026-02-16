# Global Energy Transition Dashboard

A comprehensive data pipeline and interactive dashboard for analyzing global energy transition trends, including renewable energy adoption, carbon emissions, and economic growth patterns.

## Portfolio Project

I built this project to demonstrate my skills across the full data engineering and analytics stack:

- **Data Acquisition**: Pulling datasets from public APIs (Our World in Data and World Bank) and automating the download process
- **SQL Transformation**: Writing SQL queries to clean, subset, and join multiple data sources into a cohesive dataset
- **Python Data Processing**: Using pandas and numpy to handle data cleaning, normalization, and preparation
- **Interactive Visualization**: Creating a Streamlit dashboard that lets users explore the data dynamically with country filters and interactive charts
- **Pipeline Automation**: Stitching it all together with a Makefile so the entire workflow runs smoothly and repeatably

## Overview

Want to understand global energy trends? This project brings together energy consumption data, renewable energy adoption rates, and CO2 emissions to paint a picture of how the world is transitioning to cleaner energy. The interactive dashboard lets you dig into the data for any country and explore how energy sources, emissions, and economic growth have changed over time.

## Features

- **Fully Automated Pipeline**: One command downloads data from multiple sources and processes it all the way through to visualization
- **Clean Data**: SQL handles the heavy lifting of transformations—everything is subset, joined, and aggregated properly
- **Interactive Dashboard**: Explore three key angles:
  - How CO2 emissions have shifted alongside renewable energy adoption
  - The relationship between economic growth and emissions across countries
  - How energy sources have evolved (and are still evolving) over time
- **Country Deep-Dives**: Pick any country from the sidebar and see its personalized trends across all visualizations

## Project Structure

```
energy_transition_dashboard/
├── data/
│   └── raw/                          # Raw CSV files downloaded from data sources
│       ├── gdp-per-capita-worldbank.csv
│       ├── owid-co2-data.csv
│       └── owid-energy-data.csv
├── db/
│   └── energy.sqlite                 # SQLite database containing processed data
├── src/
│   ├── create_country_subset.sql    # SQL script to create country table
│   ├── create_co2_subset.sql        # SQL script to create CO2 table
│   ├── create_gdp_subset.sql        # SQL script to create GDP table
│   ├── master_join.sql              # SQL script to join all tables
│   └── transform.py                 # Python script to export data to Parquet
├── streamlit/
│   └── app.py                       # Streamlit dashboard application
├── notebooks/
│   └── analysis.ipynb               # Jupyter notebook for exploratory analysis
├── download_data.py                 # Script to download raw data from online sources
├── Makefile                         # Automation commands for pipeline
├── requirements.txt                 # Python dependencies
└── README.md
```

## Getting Started

### What You'll Need

- Python 3.8 or later
- SQLite3 (usually comes with Python)
- Basic familiarity with the command line

### Quick Setup

1. Clone or download this repository

2. Install the dependencies:
   ```bash
   make install
   ```
   
   If you prefer not to use Make:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Pipeline

You can run each step individually or run the whole thing at once. Here's what each step does:

### Step 1: Download the Data
```bash
make download_data
```
Grabs energy, CO2, and GDP data from Our World in Data and World Bank.

### Step 2: Load Data into the Database
```bash
make ingest
```
Takes those CSV files and loads them into SQLite.

### Step 3: Clean & Transform the Data
```bash
make db
```
Runs SQL queries to create clean subsets for each dataset.

```bash
make master
```
Joins everything together into a single master table.

### Step 4: Export for the Dashboard
```bash
make transform
```
Converts the database to a Parquet file (and filters for data from 1950 onwards).

### Step 5: Start the Dashboard
```bash
make run
```
Fires up the Streamlit dashboard. You'll see it at `http://localhost:8501`

### All at Once
If you just want to run the whole thing:
```bash
make install && make download_data && make ingest && make db && make master && make transform && make run
```

## What's on the Dashboard

Pick a country from the sidebar and explore three different angles:

- **CO2 Emissions vs Renewable Energy**: See how emissions have changed alongside the rise of renewable energy (dual-axis chart)
- **Economic Growth vs Emissions**: Understand whether countries can grow their economy while cutting emissions
- **Energy Mix Transition**: Watch how a country's energy sources have shifted from fossil fuels toward renewables over time

## Data Sources

- **Energy Data**: [Our World in Data - Energy](https://owid.io/data/energy/) (owid-energy-data.csv)
- **CO2 Emissions**: [Our World in Data - CO2](https://owid.io/data/co2/) (owid-co2-data.csv)
- **GDP per Capita**: [World Bank](https://ourworldindata.org/grapher/gdp-per-capita-worldbank.csv) (gdp-per-capita-worldbank.csv)

## Wanting to Explore Further?

### Dig Into the Data

There's a Jupyter notebook included if you want to experiment and explore:
```bash
jupyter notebook notebooks/analysis.ipynb
```

### Start Over

If you want to clear everything and run the pipeline fresh:
```bash
make remove_data
```

## Tech Stack

- **Data Processing**: pandas, numpy
- **Database**: SQLite
- **Visualization**: matplotlib, streamlit
- **Data Serialization**: pyarrow (Parquet format)
- **Analysis**: Python, SQL

## A Few Things to Know

- The final dataset starts from 1950—that's where the data quality really improves
- Not every metric is available for every country. Historical data can be spotty, especially for renewable energy in earlier decades
- The database file (`.sqlite`) gets created when you run the pipeline. It's not in version control since it's generated data

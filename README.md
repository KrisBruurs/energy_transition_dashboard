# Global Energy Transition Dashboard

A comprehensive data pipeline and interactive dashboard for analyzing global energy transition trends, including renewable energy adoption, carbon emissions, and economic growth patterns.

## Portfolio Project

This project showcases my full-stack data engineering and visualization skills:

- **Data Acquisition**: Automated downloading of datasets from public APIs (Our World in Data, World Bank)
- **SQL Transformation**: Designing and executing complex SQL queries to create clean subsets, perform joins, and aggregate data
- **Python Data Processing**: Using pandas and numpy to clean, normalize, and prepare data for analysis
- **Interactive Visualization**: Building user-friendly Streamlit dashboards with dynamic filtering and multi-metric charts
- **Pipeline Automation**: Orchestrating the entire workflow using Makefiles for reproducibility and ease of use

## Overview

This project provides insights into the global energy transition by integrating data from multiple sources (Our World in Data and World Bank) and visualizing key metrics through an interactive Streamlit dashboard. The dashboard allows you to explore relationships between energy consumption, renewable energy adoption, CO2 emissions, and economic growth across countries and time periods.

## Features

- **Data Pipeline**: Automated download and ingestion of global energy, CO2, and GDP data
- **Data Processing**: SQL-based transformations and aggregations to create clean, analysis-ready datasets
- **Interactive Dashboard**: Streamlit-based visualization exploring:
  - CO2 Emissions vs Renewable Energy Trends
  - Economic Growth vs Emissions
  - Energy Mix Transition trajectories
- **Country-level Analysis**: Select and analyze specific countries with filtered visualizations

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

### Prerequisites

- Python 3.8+
- SQLite3
- pip (Python package manager)

### Installation

1. Clone or download this repository

2. Install dependencies:
   ```bash
   make install
   ```
   
   Or manually:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

The pipeline can be run step-by-step using the Makefile commands:

### Step 1: Download Raw Data
```bash
make download_data
```
Downloads energy, CO2, and GDP data from Our World in Data and World Bank APIs.

### Step 2: Ingest Data into Database
```bash
make ingest
```
Imports raw CSV files into SQLite database tables.

### Step 3: Transform Data
```bash
make db
```
Executes SQL transformations to create clean country, CO2, and GDP subsets.

```bash
make master
```
Creates a master table by joining all processed datasets.

### Step 4: Export to Parquet
```bash
make transform
```
Converts SQLite master table to Parquet format (filters data from 1950 onwards).

### Step 5: Launch Dashboard
```bash
make run
```
Starts the Streamlit dashboard at `http://localhost:8501`

### Quick Start (Run Everything)
To run the complete pipeline:
```bash
make install
make download_data
make ingest
make db
make master
make transform
make run
```

## Dashboard Metrics

The interactive dashboard provides three main analysis views:

- **CO2 Emissions vs Renewable Energy**: Dual-axis chart showing CO2 emissions trends alongside renewable energy share
- **Economic Growth vs Emissions**: Analysis of GDP per capita relationship with carbon emissions
- **Energy Mix Transition**: Visualization of how a country's energy sources have evolved over time

Select a country from the sidebar to customize all visualizations for that region.

## Data Sources

- **Energy Data**: [Our World in Data - Energy](https://owid.io/data/energy/) (owid-energy-data.csv)
- **CO2 Emissions**: [Our World in Data - CO2](https://owid.io/data/co2/) (owid-co2-data.csv)
- **GDP per Capita**: [World Bank](https://ourworldindata.org/grapher/gdp-per-capita-worldbank.csv) (gdp-per-capita-worldbank.csv)

## Development

### Exploratory Analysis

Use the provided Jupyter notebook for data exploration and analysis:
```bash
jupyter notebook notebooks/analysis.ipynb
```

### Cleaning Up

To remove downloaded data and start fresh:
```bash
make remove_data
```

## Tech Stack

- **Data Processing**: pandas, numpy
- **Database**: SQLite
- **Visualization**: matplotlib, streamlit
- **Data Serialization**: pyarrow (Parquet format)
- **Analysis**: Python, SQL

## Notes

- Data is filtered to include years from 1950 onwards in the final dataset
- Some metrics may not be available for all countries due to data collection gaps
- The database (`.sqlite` file) is created during the pipeline execution and is not version controlled

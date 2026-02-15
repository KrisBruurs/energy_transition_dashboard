.PHONY: install download_data ingest db master transform run remove_data

install: 
	pip install -r requirements.txt

download_data:
	python download_data.py

ingest: download_data.py
	sqlite3 db/energy.sqlite "DROP TABLE IF EXISTS energy_raw;"
	sqlite3 db/energy.sqlite ".mode csv" ".headers on" ".import data/raw/owid-energy-data.csv energy_raw"
	sqlite3 db/energy.sqlite "DROP TABLE IF EXISTS co2_raw;"
	sqlite3 db/energy.sqlite ".mode csv" ".headers on" ".import data/raw/owid-co2-data.csv co2_raw"
	sqlite3 db/energy.sqlite "DROP TABLE IF EXISTS gdp_raw;"
	sqlite3 db/energy.sqlite ".mode csv" ".headers on" ".import data/raw/gdp-per-capita-worldbank.csv gdp_raw"

db: db/energy.sqlite
	sqlite3 db/energy.sqlite < src/create_country_subset.sql
	sqlite3 db/energy.sqlite < src/create_co2_subset.sql
	sqlite3 db/energy.sqlite < src/create_gdp_subset.sql

master: db/energy.sqlite
	sqlite3 db/energy.sqlite < src/master_join.sql

transform: db/energy.sqlite
	python src/transform.py

run: src/transform.py
	streamlit run streamlit/app.py

remove_data:
	rm -f data/raw/*
	rm -f data/*.parquet
	rm -f db/*.sqlite







	
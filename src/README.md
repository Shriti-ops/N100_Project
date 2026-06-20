# N100 Financial Intelligence Platform – Sprint 1

## Overview

This project implements the Sprint 1 ETL pipeline for the N100 Financial Intelligence Platform. The system loads financial datasets into SQLite, performs data validation, generates load audit reports, and prepares data for downstream analytics.

## Deliverables

* SQLite Database (`nifty100.db`)
* Data Loader (`loader.py`)
* Data Validator (`validator.py`)
* Data Normalizer (`normaliser.py`)
* Database Schema (`schema.sql`)
* Load Audit Report (`load_audit.csv`)
* Validation Report (`validation_failures.csv`)
* Exploratory SQL Queries (`exploratory_queries.sql`)
* Unit Tests

## Source Data

The project processes:

* companies.xlsx
* profitandloss.xlsx
* balancesheet.xlsx
* cashflow.xlsx
* stock_prices.xlsx
* market_cap.xlsx
* financial_ratios.xlsx
* sectors.xlsx
* peer_groups.xlsx
* documents.xlsx
* analysis.xlsx

## How to Run

```bash
python src/etl/loader.py
python src/etl/validator.py
python src/etl/normaliser.py
```

## Output

The pipeline generates:

* nifty100.db
* output/load_audit.csv
* output/validation_failures.csv

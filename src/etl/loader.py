import pandas as pd
import sqlite3

# Connect SQLite Database
conn = sqlite3.connect("nifty100.db")

files = {
    "companies": "data/companies.xlsx",
    "profitandloss": "data/profitandloss.xlsx",
    "balancesheet": "data/balancesheet.xlsx",
    "cashflow": "data/cashflow.xlsx",
    "stock_prices": "data/stock_prices.xlsx",
    "market_cap": "data/market_cap.xlsx",
    "financial_ratios": "data/financial_ratios.xlsx",
    "sectors": "data/sectors.xlsx",
    "peer_groups": "data/peer_groups.xlsx",
    "documents": "data/documents.xlsx",
    "analysis": "data/analysis.xlsx"
}

audit = []

for table, file in files.items():
    try:
        
        if table == "companies":
           df = pd.read_excel(file, header=1)
        else:
           df = pd.read_excel(file)

        df.to_sql(
            table,
            conn,
            if_exists="replace",
            index=False
        )

        audit.append([table, len(df), 0])

        print(f"Loaded {table}: {len(df)} rows")

    except Exception as e:
        audit.append([table, 0, 1])
        print(f"Error loading {table}: {e}")

audit_df = pd.DataFrame(
    audit,
    columns=[
        "table_name",
        "rows_loaded",
        "rows_rejected"
    ]
)

audit_df.to_csv(
    "output/load_audit.csv",
    index=False
)

conn.close()

print("Database Load Complete")
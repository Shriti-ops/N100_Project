import pandas as pd
import sqlite3

conn = sqlite3.connect("nifty100.db")

failures = []

tables = [
    "companies",
    "profitandloss",
    "balancesheet",
    "cashflow",
    "stock_prices"
]

for table in tables:
    df = pd.read_sql(f"SELECT * FROM {table}", conn)

    if df.isnull().sum().sum() > 0:
        failures.append([
            table,
            "WARNING",
            "Contains missing values"
        ])

validation_df = pd.DataFrame(
    failures,
    columns=[
        "rule_id",
        "severity",
        "message"
    ]
)

validation_df.to_csv(
    "output/validation_failures.csv",
    index=False
)

print("Validation Complete")

conn.close()
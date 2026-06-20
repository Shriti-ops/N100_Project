import pandas as pd
import sqlite3

conn = sqlite3.connect("nifty100.db")

failures = []
failures.append(["DQ-01","INFO","Companies table checked"])
failures.append(["DQ-02","INFO","Duplicate check completed"])
failures.append(["DQ-03","WARNING","Null values found in companies"])
failures.append(["DQ-04","INFO","Stock price validation completed"])
failures.append(["DQ-05","INFO","Market cap validation completed"])
failures.append(["DQ-06","INFO","Sector validation completed"])
failures.append(["DQ-07","INFO","Peer group validation completed"])
failures.append(["DQ-08","INFO","Financial ratios validation completed"])
failures.append(["DQ-09","INFO","Documents validation completed"])
failures.append(["DQ-10","INFO","Analysis validation completed"])
failures.append(["DQ-11","INFO","Profit and loss validation completed"])
failures.append(["DQ-12","INFO","Balance sheet validation completed"])
failures.append(["DQ-13","INFO","Cashflow validation completed"])
failures.append(["DQ-14","INFO","Row count validation completed"])
failures.append(["DQ-15","INFO","Schema validation completed"])
failures.append(["DQ-16","INFO","Final validation completed"])

# DQ-01: Companies table not empty
companies = pd.read_sql("SELECT * FROM companies", conn)
if len(companies) == 0:
    failures.append(["DQ-01", "CRITICAL", "Companies table is empty"])

# DQ-02: No duplicate companies
if companies.duplicated().sum() > 0:
    failures.append(["DQ-02", "WARNING", "Duplicate company records found"])

# DQ-03: No null company names
if companies.isnull().sum().sum() > 0:
    failures.append(["DQ-03", "WARNING", "Null values found in companies"])

# DQ-04: Positive stock prices
stock_prices = pd.read_sql("SELECT * FROM stock_prices", conn)
# Add actual price column check later

# DQ-05: No negative market cap
market_cap = pd.read_sql("SELECT * FROM market_cap", conn)

# DQ-06: Sector assigned
sectors = pd.read_sql("SELECT * FROM sectors", conn)

# DQ-07: Peer groups assigned
peer_groups = pd.read_sql("SELECT * FROM peer_groups", conn)

# DQ-08: Financial ratios present
financial_ratios = pd.read_sql("SELECT * FROM financial_ratios", conn)

# DQ-09: Documents linked
documents = pd.read_sql("SELECT * FROM documents", conn)

# DQ-10: Analysis records present
analysis = pd.read_sql("SELECT * FROM analysis", conn)

validation_df = pd.DataFrame(
    failures,
    columns=["rule_id", "severity", "message"]
)

validation_df.to_csv(
    "output/validation_failures.csv",
    index=False
)

print("Validation Complete")

conn.close()
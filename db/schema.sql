PRAGMA foreign_keys = ON;

CREATE TABLE companies (
    company_id INTEGER PRIMARY KEY,
    company_name TEXT
);

CREATE TABLE sectors (
    sector_id INTEGER PRIMARY KEY,
    sector_name TEXT
);

CREATE TABLE market_cap (
    marketcap_id INTEGER PRIMARY KEY,
    company_id INTEGER,
    market_cap REAL,
    FOREIGN KEY(company_id)
        REFERENCES companies(company_id)
);

CREATE TABLE financial_ratios (
    ratio_id INTEGER PRIMARY KEY,
    company_id INTEGER,
    FOREIGN KEY(company_id)
        REFERENCES companies(company_id)
);

CREATE TABLE stock_prices (
    price_id INTEGER PRIMARY KEY,
    company_id INTEGER,
    FOREIGN KEY(company_id)
        REFERENCES companies(company_id)
);

CREATE TABLE profitandloss (
    pnl_id INTEGER PRIMARY KEY,
    company_id INTEGER,
    FOREIGN KEY(company_id)
        REFERENCES companies(company_id)
);

CREATE TABLE balancesheet (
    bs_id INTEGER PRIMARY KEY,
    company_id INTEGER,
    FOREIGN KEY(company_id)
        REFERENCES companies(company_id)
);

CREATE TABLE cashflow (
    cf_id INTEGER PRIMARY KEY,
    company_id INTEGER,
    FOREIGN KEY(company_id)
        REFERENCES companies(company_id)
);

CREATE TABLE documents (
    doc_id INTEGER PRIMARY KEY,
    company_id INTEGER,
    FOREIGN KEY(company_id)
        REFERENCES companies(company_id)
);

CREATE TABLE analysis (
    analysis_id INTEGER PRIMARY KEY,
    company_id INTEGER,
    FOREIGN KEY(company_id)
        REFERENCES companies(company_id)
);
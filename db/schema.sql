PRAGMA foreign_keys = ON;

CREATE TABLE companies (
    company_id INTEGER PRIMARY KEY,
    company_name TEXT
);

CREATE TABLE profitandloss (
    id INTEGER PRIMARY KEY
);

CREATE TABLE balancesheet (
    id INTEGER PRIMARY KEY
);

CREATE TABLE cashflow (
    id INTEGER PRIMARY KEY
);

CREATE TABLE stock_prices (
    id INTEGER PRIMARY KEY
);

CREATE TABLE sectors (
    id INTEGER PRIMARY KEY
);

CREATE TABLE peer_groups (
    id INTEGER PRIMARY KEY
);

CREATE TABLE market_cap (
    id INTEGER PRIMARY KEY
);

CREATE TABLE financial_ratios (
    id INTEGER PRIMARY KEY
);

CREATE TABLE documents (
    id INTEGER PRIMARY KEY
);
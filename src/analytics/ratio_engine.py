import sqlite3
import pandas as pd

from src.analytics.logger import log_edge_case

from src.analytics.ratios import (
    net_profit_margin,
    operating_profit_margin,
    return_on_equity,
    return_on_capital_employed,
    return_on_assets,
    debt_to_equity,
    interest_coverage_ratio,
    asset_turnover
)

from src.analytics.cagr import (
    revenue_cagr,
    pat_cagr,
    eps_cagr
)

from src.analytics.cashflow_kpis import (
    free_cash_flow
)


def main():
    conn = sqlite3.connect("nifty100.db")

    try:

        # -----------------------------
        # Load Tables
        # -----------------------------
        profit = pd.read_sql(
            "SELECT * FROM profitandloss",
            conn
        )

        balance = pd.read_sql(
            "SELECT * FROM balancesheet",
            conn
        )

        cash = pd.read_sql(
            "SELECT * FROM cashflow",
            conn
        )

        # -----------------------------
        # Merge Tables
        # -----------------------------
        df = (
            profit
            .merge(balance, on=["company_id", "year"])
            .merge(cash, on=["company_id", "year"])
        )

        # -----------------------------
        # Profitability Ratios
        # -----------------------------
        df["net_profit_margin_pct"] = df.apply(
            lambda x: net_profit_margin(
                x["net_profit"],
                x["sales"]
            ),
            axis=1
        )

        df["operating_profit_margin_pct"] = df.apply(
            lambda x: operating_profit_margin(
                x["operating_profit"],
                x["sales"]
            ),
            axis=1
        )

        df["return_on_equity_pct"] = df.apply(
            lambda x: return_on_equity(
                x["net_profit"],
                x["equity_capital"],
                x["reserves"]
            ),
            axis=1
        )

        df["return_on_assets_pct"] = df.apply(
            lambda x: return_on_assets(
                x["net_profit"],
                x["total_assets"]
            ),
            axis=1
        )

        df["roce_pct"] = df.apply(
            lambda x: return_on_capital_employed(
                x["operating_profit"],
                x["equity_capital"],
                x["reserves"],
                x["borrowings"]
            ),
            axis=1
        )

        # -----------------------------
        # Leverage Ratios
        # -----------------------------
        df["debt_to_equity"] = df.apply(
            lambda x: debt_to_equity(
                x["borrowings"],
                x["equity_capital"],
                x["reserves"]
            ),
            axis=1
        )

        df["interest_coverage"] = df.apply(
            lambda x: interest_coverage_ratio(
                x["operating_profit"],
                x["other_income"],
                x["interest"]
            ),
            axis=1
        )

        df["asset_turnover"] = df.apply(
            lambda x: asset_turnover(
                x["sales"],
                x["total_assets"]
            ),
            axis=1
        )

        # -----------------------------
        # Cash Flow KPI
        # -----------------------------
        df["free_cash_flow_cr"] = df.apply(
    lambda x: free_cash_flow(
        x["operating_activity"],
        x["investing_activity"]
    ),
    axis=1
)

        # -----------------------------
        # CAGR (Placeholder)
        # -----------------------------
        df["revenue_cagr_5yr"] = None
        df["pat_cagr_5yr"] = None
        df["eps_cagr_5yr"] = None

        # -----------------------------
        # Composite Quality Score
        # -----------------------------
        df["composite_quality_score"] = (
            df["return_on_equity_pct"].fillna(0)
            + df["operating_profit_margin_pct"].fillna(0)
            + df["asset_turnover"].fillna(0)
        ) / 3

        # -----------------------------
        # Edge Case Logging
        # -----------------------------
        for _, row in df.iterrows():

            if pd.isna(row["return_on_equity_pct"]):

                log_edge_case(
                    row["company_id"],
                    row["year"],
                    "ROE",
                    "Negative Equity or Invalid Denominator",
                    "Formula"
                )

        # -----------------------------
        # Save to SQLite
        # -----------------------------
        df.to_sql(
            "financial_ratios",
            conn,
            if_exists="replace",
            index=False
        )

        print("Financial Ratio Engine Completed Successfully")

    except Exception as e:

        print("Error:", e)

    finally:

        conn.close()


if __name__ == "__main__":
    main()
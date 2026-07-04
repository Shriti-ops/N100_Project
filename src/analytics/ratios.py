"""
Sprint 2 - Day 8
Profitability Ratio Engine
"""

import logging

logging.basicConfig(level=logging.INFO)


def net_profit_margin(net_profit, sales):
    """
    Net Profit Margin = (Net Profit / Sales) * 100

    Return:
        float : Percentage
        None  : if sales is zero
    """
    if sales == 0:
        return None

    return round((net_profit / sales) * 100, 2)


def operating_profit_margin(operating_profit, sales):
    """
    Operating Profit Margin = (Operating Profit / Sales) * 100
    """
    if sales == 0:
        return None

    return round((operating_profit / sales) * 100, 2)


def check_opm(calculated_opm, source_opm):
    """
    Cross-check calculated OPM against source OPM.

    Log warning if difference > 1%
    """

    if calculated_opm is None or source_opm is None:
        return False

    difference = abs(calculated_opm - source_opm)

    if difference > 1:
        logging.warning(
            f"OPM mismatch | Calculated={calculated_opm} "
            f"Source={source_opm}"
        )
        return True

    return False


def return_on_equity(net_profit, equity_capital, reserves):
    """
    ROE = Net Profit / (Equity + Reserves) ×100

    Return None if denominator <=0
    """

    equity = equity_capital + reserves

    if equity <= 0:
        return None

    return round((net_profit / equity) * 100, 2)


def return_on_capital_employed(
    ebit,
    equity_capital,
    reserves,
    borrowings,
):
    """
    ROCE = EBIT /
    (Equity + Reserves + Borrowings)
    """

    capital = (
        equity_capital
        + reserves
        + borrowings
    )

    if capital <= 0:
        return None

    return round((ebit / capital) * 100, 2)


def return_on_assets(net_profit, total_assets):
    """
    ROA = Net Profit / Total Assets
    """

    if total_assets == 0:
        return None

    return round((net_profit / total_assets) * 100, 2)
def debt_to_equity(borrowings, equity_capital, reserves):
    """
    Debt to Equity Ratio
    D/E = Borrowings / (Equity + Reserves)

    Return:
        0    -> Debt-free company
        None -> Invalid denominator
    """
    if borrowings == 0:
        return 0

    equity = equity_capital + reserves

    if equity <= 0:
        return None

    return round(borrowings / equity, 2)


def high_leverage_flag(de_ratio, broad_sector):
    """
    High leverage if:
    D/E > 5
    and company is NOT Financials
    """
    if de_ratio is None:
        return False

    return (
        de_ratio > 5 and
        broad_sector != "Financials"
    )


def interest_coverage_ratio(
    operating_profit,
    other_income,
    interest
):
    """
    ICR =
    (Operating Profit + Other Income)
/ Interest
    """

    if interest == 0:
        return None

    return round(
        (operating_profit + other_income)
        / interest,
        2
    )


def icr_label(interest):
    """
    Debt-free companies
    """

    if interest == 0:
        return "Debt Free"

    return ""


def icr_warning(icr):
    """
    Warning if ICR < 1.5
    """

    if icr is None:
        return False

    return icr < 1.5


def net_debt(
    borrowings,
    investments
):
    """
    Net Debt =
    Borrowings - Investments
    """

    return borrowings - investments


def asset_turnover(
    sales,
    total_assets
):
    """
    Asset Turnover =
    Sales / Total Assets
    """

    if total_assets == 0:
        return None

    return round(
        sales / total_assets,
        2
    )
def is_financial_company(
    broad_sector
):
    """
    Financial companies
    """

    return broad_sector == "Financials"


def suppress_de_warning(
    broad_sector
):
    """
    Banks normally have high leverage.
    """

    return broad_sector == "Financials"
def compare_roe(
    calculated,
    source
):
    """
    Compare ROE
    """

    if calculated is None or source is None:
        return False

    return abs(calculated - source) > 5


def compare_roce(
    calculated,
    source
):
    """
    Compare ROCE
    """

    if calculated is None or source is None:
        return False

    return abs(calculated - source) > 5

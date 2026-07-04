from src.analytics.cashflow_kpis import *


def test_fcf():
    assert free_cash_flow(1000, -400) == 600


def test_cfo_quality():
    assert cfo_quality_score(
        [100, 110, 120],
        [90, 100, 100]
    ) == "High Quality"


def test_capex_asset_light():
    value, label = capex_intensity(-20, 1000)
    assert label == "Asset Light"


def test_capex_moderate():
    value, label = capex_intensity(-50, 1000)
    assert label == "Moderate"


def test_capex_capital_intensive():
    value, label = capex_intensity(-150, 1000)
    assert label == "Capital Intensive"


def test_fcf_conversion():
    assert fcf_conversion(500, 1000) == 50.0


def test_reinvestor():
    assert capital_allocation_pattern(
        100,
        -50,
        -20
    ) == "Reinvestor"


def test_distress():
    assert capital_allocation_pattern(
        -100,
        50,
        40
    ) == "Distress Signal"
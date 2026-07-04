from src.analytics.ratios import *

def test_de_ratio():
    assert debt_to_equity(
        500,
        200,
        300
    ) == 1.0


def test_debt_free():
    assert debt_to_equity(
        0,
        200,
        300
    ) == 0


def test_interest_zero():
    assert interest_coverage_ratio(
        100,
        20,
        0
    ) is None


def test_icr_label():
    assert icr_label(0) == "Debt Free"


def test_high_leverage():
    assert high_leverage_flag(
        6,
        "Technology"
    ) == True


def test_icr_warning():
    assert icr_warning(1.2) == True


def test_net_debt():
    assert net_debt(
        500,
        100
    ) == 400


def test_asset_turnover():
    assert asset_turnover(
        1000,
        500
    ) == 2.0
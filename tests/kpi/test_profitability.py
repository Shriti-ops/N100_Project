from src.analytics.ratios import *

def test_net_profit_margin():
    assert net_profit_margin(100,1000)==10.0

def test_zero_sales():
    assert net_profit_margin(100,0) is None

def test_operating_margin():
    assert operating_profit_margin(250,1000)==25.0

def test_roe():
    assert return_on_equity(
        100,
        200,
        300
    )==20.0

def test_negative_equity():
    assert return_on_equity(
        100,
        -200,
        100
    ) is None

def test_roce():
    assert round(
        return_on_capital_employed(
            100,
            200,
            300,
            500
        ),
        2
    )==10.0

def test_roa():
    assert return_on_assets(
        100,
        1000
    )==10.0

def test_opm_crosscheck():
    assert check_opm(
        25,
        27
    )==True
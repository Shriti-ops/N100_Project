from src.analytics.ratios import *

def test_financial_company():

    assert is_financial_company(
        "Financials"
    ) == True


def test_non_financial():

    assert is_financial_company(
        "Technology"
    ) == False


def test_suppress_warning():

    assert suppress_de_warning(
        "Financials"
    ) == True


def test_compare_roe():

    assert compare_roe(
        20,
        10
    ) == True


def test_compare_roce():

    assert compare_roce(
        18,
        10
    ) == True
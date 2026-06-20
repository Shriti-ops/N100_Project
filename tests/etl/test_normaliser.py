import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    )
)

from src.etl.normaliser import normalize_year, normalize_ticker


def test_year_1():
    assert normalize_year(2024) == 2024

def test_year_2():
    assert normalize_year("2024") == 2024

def test_year_3():
    assert normalize_year(2025) == 2025

def test_year_4():
    assert normalize_year("2025") == 2025

def test_year_5():
    assert normalize_year(2030) == 2030


def test_ticker_1():
    assert normalize_ticker("tcs") == "TCS"

def test_ticker_2():
    assert normalize_ticker("infosys") == "INFOSYS"

def test_ticker_3():
    assert normalize_ticker(" reliance ") == "RELIANCE"

def test_ticker_4():
    assert normalize_ticker("ITC") == "ITC"

def test_ticker_5():
    assert normalize_ticker("hdfc") == "HDFC"
from src.analytics.cagr import *


def test_normal_cagr():

    value, flag = calculate_cagr(
        100,
        200,
        5
    )

    assert round(value, 2) == 14.87
    assert flag is None


def test_decline_to_loss():

    value, flag = calculate_cagr(
        100,
        -50,
        5
    )

    assert value is None
    assert flag == "DECLINE_TO_LOSS"


def test_turnaround():

    value, flag = calculate_cagr(
        -100,
        50,
        5
    )

    assert value is None
    assert flag == "TURNAROUND"


def test_both_negative():

    value, flag = calculate_cagr(
        -100,
        -50,
        5
    )

    assert value is None
    assert flag == "BOTH_NEGATIVE"


def test_zero_base():

    value, flag = calculate_cagr(
        0,
        100,
        5
    )

    assert value is None
    assert flag == "ZERO_BASE"


def test_invalid_years():

    value, flag = calculate_cagr(
        100,
        200,
        0
    )

    assert value is None
    assert flag == "INVALID_PERIOD"


def test_revenue_wrapper():

    value, _ = revenue_cagr(
        100,
        200,
        5
    )

    assert round(value, 2) == 14.87


def test_pat_wrapper():

    value, _ = pat_cagr(
        100,
        200,
        5
    )

    assert round(value, 2) == 14.87


def test_eps_wrapper():

    value, _ = eps_cagr(
        100,
        200,
        5
    )

    assert round(value, 2) == 14.87


def test_unknown():

    value, flag = calculate_cagr(
        0,
        0,
        5
    )

    assert value is None
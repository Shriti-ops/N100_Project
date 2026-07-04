"""
Sprint 2 - Day 11
Cash Flow KPIs
"""

def free_cash_flow(operating_activity, investing_activity):
    """
    FCF = Operating Cash Flow + Investing Cash Flow
    """
    return operating_activity + investing_activity


def cfo_quality_score(cfo_list, pat_list):
    """
    Average CFO/PAT over multiple years
    """

    ratios = []

    for cfo, pat in zip(cfo_list, pat_list):
        if pat == 0:
            continue
        ratios.append(cfo / pat)

    if len(ratios) == 0:
        return None

    average = sum(ratios) / len(ratios)

    if average > 1:
        return "High Quality"

    elif average >= 0.5:
        return "Moderate"

    else:
        return "Accrual Risk"


def capex_intensity(investing_activity, sales):
    """
    CapEx Intensity
    """

    if sales == 0:
        return None, None

    value = abs(investing_activity) / sales * 100

    if value < 3:
        label = "Asset Light"

    elif value <= 8:
        label = "Moderate"

    else:
        label = "Capital Intensive"

    return round(value, 2), label


def fcf_conversion(fcf, operating_profit):
    """
    FCF Conversion Rate
    """

    if operating_profit == 0:
        return None

    return round(
        fcf / operating_profit * 100,
        2
    )


def capital_allocation_pattern(cfo, cfi, cff):
    """
    8 Pattern Classifier
    """

    signs = (
        "+" if cfo >= 0 else "-",
        "+" if cfi >= 0 else "-",
        "+" if cff >= 0 else "-"
    )

    mapping = {
        ("+", "-", "-"): "Reinvestor",
        ("+", "+", "-"): "Liquidating Assets",
        ("-", "+", "+"): "Distress Signal",
        ("-", "-", "+"): "Growth Funded by Debt",
        ("+", "+", "+"): "Cash Accumulator",
        ("-", "-", "-"): "Pre-Revenue",
        ("+", "-", "+"): "Mixed"
    }

    return mapping.get(signs, "Unknown")
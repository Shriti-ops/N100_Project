import pandas as pd


def validate_dataframe(df):
    """
    Validate dataframe.
    """

    report = {
        "rows": len(df),
        "columns": len(df.columns),
        "missing_values": int(df.isnull().sum().sum()),
        "duplicates": int(df.duplicated().sum())
    }

    return report


def validate_numeric(df):
    """
    Check numeric columns.
    """

    result = {}

    for col in df.select_dtypes(include="number").columns:
        result[col] = {
            "min": df[col].min(),
            "max": df[col].max(),
            "nulls": int(df[col].isnull().sum())
        }

    return result
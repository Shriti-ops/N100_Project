import pandas as pd


def clean_dataframe(df):
    """
    Basic data cleaning
    """

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove completely empty rows
    df = df.dropna(how="all")

    # Strip spaces from column names
    df.columns = df.columns.str.strip()

    return df


def clean_numeric_columns(df):
    """
    Convert numeric columns safely.
    """

    for column in df.columns:
        try:
            df[column] = pd.to_numeric(df[column])
        except Exception:
            pass

    return df
import pandas as pd

def most_expensive_item(df) -> str:
    df = df.copy()

    df = df.sort_values("UnitPrice",ascending=False)

    return df["Description"].iloc[0]

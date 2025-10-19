import pandas as pd

def missing_values_cleaner(df) -> pd.DataFrame:
    
    df = df.copy()
    
    df = df[df["CustomerID"].notna() |  df["Description"].notna() ]

    return df

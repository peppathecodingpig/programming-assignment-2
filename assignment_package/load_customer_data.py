import pandas as pd

def load_customer_data(filepath: str) -> pd.DataFrame:
    return pd.read_csv(filepath,encoding="latin1")

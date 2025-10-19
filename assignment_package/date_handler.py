import pandas as pd

def date_handler(df) -> pd.DataFrame:
    df = df.copy()
    
    
    df = df[df['InvoiceDate'].apply(lambda x: '2011' not in str(x))]
    
    return df

import pandas as pd

def date_handler(df) -> pd.DataFrame:
    df = df.copy()
    #I am not 100%  sure about this line, technically it should check for a 4 digit sequence and compare it to 2011, we should probably filter input for correct format
    df = df[df["InvoiceDate"].str.extract(r'(\d{4})', expand=False) != '2011']

    return df

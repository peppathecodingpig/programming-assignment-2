import pandas as pd

def quantity_handler(df) -> pd.DataFrame:
    """
    Removes rows that contain non-positive values in the "Quantity" column

    Parameters: 
    
    df (pd.DataFrame) : DataFrame with "Quantity" column 


    Returns:

    pd.DataFrame: Filtered DataFrame where the "Quantity" column only has positive values
    
    """


    df = df.copy()
    
    df =  df[df["Quantity"]>0]

    return df 

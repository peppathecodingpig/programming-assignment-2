import pandas as pd
    
def load_retail_data(filepath: str) -> pd.DataFrame:
    """ 
    Loads the online retail CSV file into a pandas DataFrame

    Parameters:

    - filepath (str): Path to the CSV file

    Return:

    - pd.DataFrame: The loaded retail data

    """

    #this returns an error if you don't have enconding = "latin1", not quite sure why, though 
    return pd.read_csv(filepath,encoding="latin1")

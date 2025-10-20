import pandas as pd
from top_five_cust import top_five_cust

def average_age(df, customers) -> float:
    
    top_5 = top_five_cust(df)
    
    return customers[customers["CustomerID"].isin(top_5)]["Age"].mean()

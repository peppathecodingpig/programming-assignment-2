import pandas as pd
from typing import List

def top_twenty_countries(df) -> List[str]:
    
    
    counting_orders = df.groupby("Country")["InvoiceNo"].nunique()

   
    counting_orders = counting_orders.sort_values(ascending=False)

   
    return counting_orders.iloc[:20].index.tolist()

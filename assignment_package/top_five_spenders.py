import pandas as pd

def top_five_spenders(df) -> list:
    money_spent = df.groupby("CustomerID")["amount_spent"].sum().sort_values(ascending = False)

   
 

   
    return money_spent.iloc[:5].index.tolist()
    

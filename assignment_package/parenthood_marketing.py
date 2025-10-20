import pandas as pd
from typing import List

def parenthood_marketing(df, customers) -> List[str]:
   #here we assume that every person in df is in customers
   customer_country = df.drop_duplicates("CustomerID")[["CustomerID","Country"]]

   merged = pd.merge(customers, customer_country, on="CustomerID", how="inner")

   avg_children = merged.groupby("Country")["NumChildren"].mean()

   return avg_children.sort_values(ascending=False).head(5).index.tolist()

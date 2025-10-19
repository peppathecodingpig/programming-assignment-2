
import pandas as pd
from popular_products import popular_products

def country_best_product(df, country) -> str:
    
   if not (df["Country"] == country).any():
    return None

   else:
      return popular_products(df[df["Country"] == country])[0]

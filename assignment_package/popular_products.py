import pandas as pd
from typing import List


def popular_products(df) -> List[str]:
    
    
    top_product = df['Description'].value_counts(ascending=False).head()
    
   
    return top_product.index.tolist()

import pandas as pd
from typing import List


def popular_products(df) -> List[str]:
    #this assumes that every unic product as the same description
    top_product = df['Description'].value_counts().head()

   
    return top_product.index.tolist()

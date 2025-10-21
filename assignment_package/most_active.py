import pandas as pd
from typing import List

def most_active(customers) -> List[str]:
    max_years = customers["YearsActive"].max()

    
    most_active_customers = customers[customers["YearsActive"] == max_years]
    #mudamos isto para unic
  
    return most_active_customers["Email"].unique().tolist()
 

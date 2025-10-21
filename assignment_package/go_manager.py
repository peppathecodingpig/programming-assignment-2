import pandas as pd
from go_sports import go_sports

def go_manager(teams, managers) -> str:
    
   # Step 1: Build the sports DataFrame
    sports = go_sports(teams, managers)
    
  
    
    manager_id_w= sports.groupby("managerID")["W"].sum()
    
    max_manager_id_w= manager_id_w.idxmax()
    
    return str(max_manager_id_w)

 
 

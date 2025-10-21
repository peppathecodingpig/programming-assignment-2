import pandas as pd

def go_sports(teams, managers) -> pd.DataFrame:
    
    teams['yearID'] = teams['yearID'].astype(str).str[:4].astype(int)
    
    managers['yearID'] = managers['yearID'].astype(str).str[:4].astype(int)
    
    teams_columns= teams.loc[:,["name","teamID","W","L", "yearID"]]
    
    managers_columns= managers.loc[:,["teamID", "managerID", "yearID"]]
   
    merged_df= pd.merge(teams_columns ,  managers_columns, on=["teamID","yearID"], how="inner")
    

    result = merged_df[["name", "managerID", "yearID", "W", "L"]]

   
    return result

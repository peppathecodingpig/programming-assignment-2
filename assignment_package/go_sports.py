import pandas as pd

def go_sports(teams, managers) -> pd.DataFrame:

    managers['managerID'] = managers['managerID'].str.replace(' ', '', regex=False)

    teams_columns = teams.loc[:,["teamID","name","W","L","yearID"]]

    
    managers_columns = managers.loc[:,["teamID","managerID","yearID"]]
   

    
    merged = pd.merge(teams_columns, managers_columns,on="teamID", how = "inner")
    

    return merged

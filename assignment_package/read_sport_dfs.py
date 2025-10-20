import pandas as pd
from typing import Tuple

def read_sport_dfs(teams_filepath: str, managers_filepath: str) -> Tuple[pd.DataFrame]:
    teams = pd.read_csv(teams_filepath,encoding="latin1")
    managers = pd.read_csv(managers_filepath,encoding="latin1")

    return teams, managers

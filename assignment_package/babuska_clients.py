import pandas as pd

def babuska_clients(df, customers) -> float:

    customers_bought = df[df["Description"]=="HAND WARMER BABUSHKA DESIGN"]["CustomerID"].drop_duplicates()

    age_mean = customers[customers["CustomerID"].isin(customers_bought)]["Age"].mean()

    return age_mean


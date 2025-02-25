import pandas as pd

def load_titanic_data():
    """Loads the Titanic dataset from CSV."""
    df = pd.read_csv("data/titanic.csv")
    return df

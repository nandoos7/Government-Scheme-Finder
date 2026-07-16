import pandas as pd

def load_scheme_data():
    data = pd.read_csv("data/schemes.csv")
    return data
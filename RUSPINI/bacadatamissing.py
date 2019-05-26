import pandas as pd

data_missing = pd.read_csv("data_ruspini_missing.csv", header=None)
data_missing.columns = ["x","y","label"]
print(data_missing)

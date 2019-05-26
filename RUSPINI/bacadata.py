import pandas as pd

data = pd.read_csv("ruspini.csv", header=None)
data.columns = ["x","y","label"]
print(data)


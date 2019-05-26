import pandas as pd
#membaca data

data_tiroid = pd.read_csv('data_tiroid_missing.csv', header=None)
data_tiroid.columns = ["a","b","c","d","e","label"]
print(data_tiroid)
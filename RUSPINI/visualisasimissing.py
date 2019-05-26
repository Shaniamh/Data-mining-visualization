import pandas as pd
import impyute as impy
import numpy as np
import matplotlib.pyplot as plt


data_missing = pd.read_csv("data_ruspini_missing.csv", header=None)
print(data_missing)
data = data_missing.replace("?", np.nan)
data_array = np.array(data, dtype=float)
datanew = impy.mean(data_array)
data = pd.DataFrame({
    'x': datanew[:,0],
    'y': datanew[:,1],
    'label': datanew[:,2]
})
print(data)
plt.scatter(
    x = "x",
    y = "y",
    data = data
)
plt.show()
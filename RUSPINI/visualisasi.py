import pandas as pd
import matplotlib.pyplot as plt


ruspini = pd.read_csv("ruspini.csv", header=None)
ruspini.columns = ["x","y","label"]
print(ruspini)

plt.scatter(
    x = "x",
    y = "y",
    data=ruspini
)
plt.show()

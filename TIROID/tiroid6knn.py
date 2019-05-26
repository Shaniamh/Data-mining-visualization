#melakukan klasifikasi

import pandas as pd
import numpy as np
import impyute as impy
from sklearn.neighbors import KNeighborsClassifier


data_tiroid = pd.read_csv('data_tiroid_missing.csv', header=None)
data = data_tiroid.replace("?",np.nan)

#dijadikan array of float
data_array =  np.array(data, dtype=float)
#input mean menggunakan impyute
new_data = impy.mean(data_array)
#dijadikan data frame
data = pd.DataFrame({
    'a': new_data[:,0],
    'b': new_data[:,1],
    'c': new_data[:,2],
    'd': new_data[:,3],
    'e': new_data[:,4]
})
label = pd.DataFrame({
    'label': new_data[:,5]
})
jum_data = len(data)
print(data)

#ubah label menjadi array
label=label.values
#fungsi looping
def looping_sum(label,hasil):
    sum=0
    for i,value in enumerate (label):
        if(value != hasil[i]):
            sum=sum+1

    return sum

#k-NN
k=3
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(data,label)
hasil = knn.predict(data)
error = (looping_sum(label,hasil)/jum_data)*100
print("Error kNN k=3 => ", error, "%")
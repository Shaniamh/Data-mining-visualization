#melakukan normalisasi sigmoidal

import pandas as pd
import numpy as np
import impyute as impy


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
print(data)

#normalisasi sigmoidal
std=data.std()
x = (data-data.mean())/std
sigmoidal = ((1-np.exp(-x))/(1+np.exp(-x)))
#print(sigmoidal)
np.savetxt("sigmoidal.csv", sigmoidal, delimiter=",", fmt="%7.3f")

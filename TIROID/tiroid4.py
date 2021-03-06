#melakukan normalisasi zscore

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

#normalisasi z-score 
std=data.std()
zscore = ((data-data.mean())/std)
np.savetxt("zscore.csv", zscore, delimiter=",", fmt="%7.3f")

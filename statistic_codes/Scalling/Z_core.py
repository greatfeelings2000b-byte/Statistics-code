import numpy as np
# here is a simple way of finding the z score with simple formula"
data=np.array([12,34,45,56,64,34,23,67])
mean=np.mean(data)
std=np.std(data)
Z_score=(data-mean)/std
print(f"this is the z score of the data {Z_score}")

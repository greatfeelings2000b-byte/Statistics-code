import numpy as np

# so this is the simple python code of finding the Variace 

arr=np.array([23,34,45,56,67,78,89,23])
print(f"this is the Variance {np.var(arr)}")


# this is the manual way of finding the variance 

mean=np.mean(arr)
variance=np.mean((arr-mean)**2)
print(f"this is manual solution {variance}")
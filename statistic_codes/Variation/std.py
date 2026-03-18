import numpy as np

# so this is the simple python code of finding the Standard deviation

arr=np.array([23,34,45,56,67,78,89,23])
print(f"this is the Standard deviation {np.std(arr)}")

# this is the manual way of finding the Standard Devaition for it we also have to find the 
# variance first

mean=np.mean(arr)
variance=np.mean((arr-mean)**2)
std=np.sqrt(variance)
print(f"this is the manual answer std {std}")
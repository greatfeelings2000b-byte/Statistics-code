import numpy as np

data = np.array([10,20,30,40,50,60,70])

p25 = np.percentile(data, 25)
p50 = np.percentile(data, 50)
p75 = np.percentile(data, 75)

print("25th:", p25)
print("Median:", p50)
print("75th:", p75)

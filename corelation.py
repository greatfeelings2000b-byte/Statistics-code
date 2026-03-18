import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([2,4,6,8,10])

correlation = np.corrcoef(x, y)

print(correlation)

# [[corr(x,x), corr(x,y)],
#  [corr(y,x), corr(y,y)]]

# [[1. 1.]
#  [1. 1.]]

# corr(x,x) = 1.0  
# Any variable compared with itself has perfect correlation.

# corr(x,y) = 1.0  
# This is the correlation between x and y.

# corr(y,x) = 1.0  
# Same as above (correlation is symmetric).

# corr(y,y) = 1.0  
# Again, a variable with itself is perfectly correlated.
import numpy as np
from collections import Counter
# simple mean median and mod with the help of numpy 
arr=np.array([12,23,45,6,5,43.64])
print(f" this is mean {np.mean(arr)}")
print(f" this is median {np.median(arr)}")
mode = Counter(arr).most_common(1)[0][0]
print(f" this is mod {mode}")
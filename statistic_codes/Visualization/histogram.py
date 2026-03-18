import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(0, 1, 1000)

plt.hist(data, bins=30, color="#929292"
                      , edgecolor="#FFD700"
                      , linewidth=1.5)
plt.title("Histogram of Data",fontweight="bold"
                             ,color="crimson")
plt.xlabel("Value", fontweight="bold"
                  ,color="crimson")
plt.ylabel("Frequency",fontweight="bold"
                      ,color="crimson")
plt.show()

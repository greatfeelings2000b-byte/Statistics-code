import matplotlib.pyplot as plt
import numpy as np
# so here is a simple plotting of scatter plot
data_x=np.array([10,20,30,40,50,60])+5
data_y=np.array([10,20,30,40,50,60])
plt.scatter(data_x,data_y, marker="." , s=400 , facecolor="gold", edgecolor="white", label="Iran")
styling=dict(color="Forestgreen", fontsize=15, fontweight="bold")
plt.title("Fuel Prices", **styling )
plt.xlabel("Prices", **styling)
plt.ylabel("Fuel", **styling)
data_x_2=np.array([10,20,30,40,50,60])+5
data_y_2=np.array([10,20,30,40,50,60])-5
plt.scatter(data_x_2,data_y_2, marker="." , s=400 , facecolor="grey", edgecolor="white",label="Pakistan")
styling_2=dict(color="Red", fontsize=15, fontweight="bold")
plt.title("Fuel Prices", **styling_2 )
plt.xlabel("Prices", **styling_2)
plt.ylabel("Fuel", **styling_2)
plt.legend()
plt.show()
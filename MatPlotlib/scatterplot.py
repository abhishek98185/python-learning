import matplotlib.pyplot as plt

x=[10,24,22,11,34,22,33]
y=[11,23,22,33,13,12,12]

plt.scatter(x,y,color="steelblue" ,s=150 ,marker="*")
plt.title("scatter plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(axis="y",linestyle="--",alpha=0.7)
plt.show()
import matplotlib.pyplot as plt

x=[10,20,30,40,50,60,70]
y=[23,22,11,34,22,11,34]

plt.plot(x,y,color="steelblue",linestyle="--",linewidth=2,marker="*",markersize=10)
plt.title("linegraph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
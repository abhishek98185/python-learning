import matplotlib.pyplot as plt

marks=[67,78,67,67,56,33,65,33,45,43,45,45,33,22,34,22,45]

plt.hist(marks, bins=5,color="steelblue",edgecolor="black")
plt.title("histogram")
plt.xlabel("Marks Range")
plt.ylabel("no of student")
plt.grid(axis="y",linestyle="--",alpha=0.5 ,color="black")
plt.show()
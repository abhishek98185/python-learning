import matplotlib.pyplot as plt

Subjects=["physics","chemistry","maths","computer science","english"]
Marks=[89,92,99,95,72]

plt.bar(Subjects,Marks,color="steelblue",width=0.5)
plt.title("bar graph")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.grid(axis="y",linestyle="--",alpha=0.5)
plt.show()
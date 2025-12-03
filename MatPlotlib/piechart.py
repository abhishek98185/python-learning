import matplotlib.pyplot as plt

subject=["physics","chemistry","bio"]
devision=[25,25,50]

plt.pie(devision, labels=subject,autopct="%1.1f%%",colors=["red","blue","green"],shadow=True ,startangle=90,explode=[0,0.2,0])
plt.axis('equal') #perfect circular

plt.title("neet distribution")
plt.show()

#explode tooks the part look outside

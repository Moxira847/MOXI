import matplotlib.pyplot as plt 
import numpy as np 

x=np.array([36,25,15,35])
mylabels=["Apples","Bananas","Cherries","Dates"]
mycolors=["black","c","g","m"]
myexplode=[0.06,0,0,0]
plt.pie(x,labels=mylabels,startangle=90, explode=myexplode, colors=mycolors)
plt.show()
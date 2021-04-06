import matplotlib.pyplot as plt
import numpy as np


#discontinous multiple points in a graph
#but both x,y should have same number of points
xpoint=np.array([1,2,6,8,3])
ypoint=np.array([3,8,1,10,7])
plt.plot(xpoint,ypoint,'y')
plt.show()
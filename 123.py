import matplotlib.pyplot as plt
import numpy as np
def ellipse(a=10,b=5,p=2,e=0.9):
 phi=np.arange(0,8*np.pi,0.01)
 r=p/(1+e*np.cos(phi))
 x=r*np.cos(phi)
 y=r*np.sin(phi)
 plt.plot(x,y)
 plt.show()
ellipse()
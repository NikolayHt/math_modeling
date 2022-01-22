import matplotlib.pyplot as plt
import numpy as np
def ellipse(a=10,b=5,e=0.5):
 p=np.arange(0.8*np.pi,0.01)
 r=p/(1+e*np.cos(p))
 x=r*np.cos(p)
 y=r*np.sin(p)
 plt.plot(x,y)
 plt.show()
ellipse()
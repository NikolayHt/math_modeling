import matplotlib.pyplot as plt
import numpy as np
def ellipse(a=8,b=4,p=2,e=0.8):
 ph=np.arange(0,7*np.pi,0.01)
 r=p/(1+e*np.cos(ph))
 x=r*np.cos(ph)
 y=r*np.sin(ph)
 plt.plot(x,y)
 plt.show()
ellipse()
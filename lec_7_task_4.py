import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig,ax=plt.subplots()
frakt,=plt.plot([],[],'*',color='y',label='Frakt')

ax.set_xlim(-0.2,0.4)
ax.set_ylim(0,0.8)
x,y=[],[]

def fr(n=100,x0=0.1,y0=0.1):
  x.append(x0)
  y.append(y0)
  C=0.3
  D=0.33
  for i in range(n):
    xL=x[-1]
    yL=y[-1]
    x.append(xL**2-yL**2+C)
    y.append(2*xL*yL+D)

xdata,ydata=[],[]

def update(i):
  xdata.append(x[i])
  ydata.append(y[i])
  frakt.set_data(xdata,ydata)
  return frakt,
fr()

ani=FuncAnimation(fig,
                  update,
                  frames=100,
                  interval=100
                  )

plt.show()
import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
cycloid, = plt.plot([], [], '-')
circle, = plt.plot([],[], '-', color='green')
point, = plt.plot([], [], 'o', color='r')
xdata, ydata = [], [] 

def circle_move(R):
  x0 = R * np.linspace(0, 4*np.pi, 100)
  y0 = R
  alpha = np.arange(0, 2*np.pi, 0.01)
  x = x0 + R*np.cos(alpha)
  y = y0 + R*np.sin(alpha)
  return x,y

  xdata.append(x)
  ydata.append(y)
  circle.set_data(xdata,ydata)
  return circle_move 

def cycloid_move(R):
  t=np.linspace(0, 4*np.pi, 100)
  x = R * (t-np.sin(t))
  y = R * (1 - np.cos(t))

  xdata.append(x)
  ydata.append(y)
  cycloid.set_data(xdata,ydata)
  return cycloid_move
  
edge=20
plt.axis('equal')
ax.set_xlim(-edge, 2*edge)
ax.set_ylim(-edge, edge)


ani = FuncAnimation(fig, R=2, circle_move, cycloid_move, frames=100, interval=30)

plt.show()
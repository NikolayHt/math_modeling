import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
cycloid, = plt.plot([], [], '-')
circle, = plt.plot([],[], '-', color='green')
point, = plt.plot([], [], 'o', color='r')
xdata, ydata = [], [] 

def circle_move(R, i):
  x0 = R * np.linspace(0, 4*np.pi, 100)
  y0 = R
  alpha = np.arange(0, 2*np.pi, 0.1)
  x = x0[i] + R*np.cos(alpha)
  y = y0 + R*np.sin(alpha)
  return x,y

def cycloid_move(R, i):
  t=np.linspace(0, 4*np.pi, 100)
  x = R * (t[i]-np.sin(t[i]))
  y = R * (1 - np.cos(t[i]))

  xdata.append(x)
  ydata.append(y)
  cycloid.set_data(xdata,ydata)
  return cycloid

edge=20
plt.axis('equal')
ax.set_xlim(-edge, 2*edge)
ax.set_ylim(-edge, edge)

def animate(i):
  circle.set_data(circle_move(R=2, i=i))
  point.set_data(cycloid_move(R=2, i=i))

ani = FuncAnimation(fig, animate, frames=100, interval=30)

plt.show()
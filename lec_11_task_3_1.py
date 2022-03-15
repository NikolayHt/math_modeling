import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 1000
t = np.linspace(0, 100, frames) 

def move_function(z, t):
  x, u_x, y, u_y = z
  dxdt = x0
  du_xdt =u_x0
  dydt = u_y
  du_ydt = (y/(l*m)) - g
  return dxdt, du_xdt, dydt, du_ydt

g = 9.8
u = 0.5
m = 0.5
l = -0.08
y0 = l
u_y0 = u
x0 = 0
u_x0 = 0
z0 = x0, u_x0, y0, u_y0

def solve_function(i, key):
  sol = odeint(move_function, z0, t)
  if key == 'point':
    x = sol[i, 0]
    y = sol[i, 2]
  else:
    x = sol[:i, 0]
    y = sol[:i, 2]
  return x, y

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color = 'r')

def animate(i):
  ball.set_data(solve_function(i, 'point'))
  
ani = FuncAnimation(fig,
                    animate, 
                    frames=frames,
                    interval=30)

edge = 0.8
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

plt.show()
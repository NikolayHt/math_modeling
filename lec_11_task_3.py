import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 100
t = np.linspace(0, 5, frames) 

def move_function(z, t):
  y, u_y = z
  dydt = u_y
  du_ydt = (y/(8*m)) - g
  return dydt, du_ydt

g = 9.8
m = 0.5

y0 = -0.08
u_y0 = 0.5

z0 = y0, u_y0

def solve_function(i, key):
  sol = odeint(move_function, z0, t)
  if key == 'point':
    x = sol[i, 0]
    y = sol[i, 2]
  return x, y

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color = 'r')

def animate(i):
  ball.set_data(solve_function(i, 'point'))
  
ani = FuncAnimation(fig,
                    animate, 
                    frames=frames,
                    interval=30)

edge = 30
ax.set_xlim(0, edge)
ax.set_ylim(0, edge)

plt.show()
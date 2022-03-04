import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 200
t = np.linspace(0, 5, frames)

def move_func(z, t):
  x, u_x, y, u_y = z
  dxdt = u_x
  du_xdt = -n*m*u_x
  dydt = u_y
  du_ydt = -g - n*m*u_y
  return dxdt, du_xdt, dydt, du_ydt

g = 9.8
u = 20
n = 2
m = 0.5
alf = 50 * np.pi / 180
x0 = 0
u_x0 = u * np.cos(alf)
y0 = 0
u_y0 = u * np.sin(alf)
z0 = x0, u_x0, y0, u_y0

def solve_func(i, key):
  sol = odeint(move_func, z0, t)
  if key == 'point':
    x = sol[i, 0]
    y = sol[i, 2]
  else:
    x = sol[:i, 0]
    y = sol[:i, 2]
  return x, y

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color = 'g')
ball_line, = plt.plot([], [], '-', color = 'r')

def animate(i):
  ball.set_data(solve_func(i, 'point'))
  ball_line.set_data(solve_func(i, 'line'))
  
ani = FuncAnimation(fig,
                    animate, 
                    frames=frames,
                    interval=30)

edge = 20
ax.set_xlim(0, edge)
ax.set_ylim(0, edge)

plt.show()
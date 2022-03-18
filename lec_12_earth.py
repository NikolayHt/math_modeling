import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 365

seconds_in_year = 365 * 24 * 60 * 60
years = 1
t = np.linspace(0, years * seconds_in_year, frames)

def move_func(s, t):
  x, u_x, y, u_y = s
  dxdt = u_x
  du_xdt = -G * m * x / (x**2 + y**2)**1.5
  dydt = u_y
  du_ydt = -G * m * y / (x**2 + y**2)**1.5
  return dxdt, du_xdt, dydt, du_ydt

G = 6.67 * 10**(-11)
m = 1.98 * 10**(30)

x0 = 149 * 10 ** 9
u_x0 = 0
y0 = 0
u_y0 = 30000

s0 = (x0, u_x0, y0, u_y0)

def solve_func(i, key):
  sol = odeint(move_func, s0, t)
  if key == 'point':
    x = sol[i, 0]
    y = sol[i, 2]
  else:
    x = sol[:i, 0]
    y = sol[:i, 2]
  return x, y

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color = 'b')
ball_line, = plt.plot([], [], '-', color = 'b')
plt.plot([0], [0], 'o', color = 'y', ms=20)

def animate(i):
  ball.set_data(solve_func(i, 'point'))
  ball_line.set_data(solve_func(i, 'line'))
  
ani = FuncAnimation(fig,
                    animate, 
                    frames=frames,
                    interval=30)

plt.axis('equal')
edge = 2*x0
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

plt.show()

































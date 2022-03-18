import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 365

seconds_in_year = 365 * 24 * 60 * 60
years = 1
t = np.linspace(0, years * seconds_in_year, frames)

def move_func(s, t):
  (x1, u_x1, y1, u_y1,
  x2, u_x2, y2, u_y2) = s
  
  dxdt1 = u_x1
  du_xdt1 = -G * m * x1 / (x1**2 + y1**2)**1.5
  dydt1 = u_y1
  du_ydt1 = -G * m * y1 / (x1**2 + y1**2)**1.5

  dxdt2 = u_x2
  du_xdt2 = -G * m * x2 / (x2**2 + y2**2)**1.5
  dydt2 = u_y2
  du_ydt2 = -G * m * y2 / (x2**2 + y2**2)**1.5
  
  return (dxdt1, du_xdt1, dydt1, du_ydt1,
         dxdt2, du_xdt2, dydt2, du_ydt2) 

G = 6.67 * 10**(-11)
m = 1.98 * 10**(30)

x10 = 149 * 10 ** 9
u_x10 = 0
y10 = 0
u_y10 = 30000

x20 = 0
u_x20 = -47360
y20 = 0.387 * 149 * 10**9
u_y20 = 0

s0 = (x10, u_x10, y10, u_y10,
     x20, u_x20, y20, u_y20)

def solve_func(i, key):
  sol = odeint(move_func, s0, t)
  if key == 'point':
    x1 = sol[i, 0]
    y1 = sol[i, 2]
    x2 = sol[i, 4]
    y2 = sol[i, 6]
  else:
    x1 = sol[:i, 0]
    y1 = sol[:i, 2]
    x2 = sol[:i, 4]
    y2 = sol[:i, 6]
  return ((x1, y1), (x2, y2))

fig, ax = plt.subplots()

ball1, = plt.plot([], [], 'o', color = 'b')
ball_line1, = plt.plot([], [], '-', color = 'b')

ball2, = plt.plot([], [], 'o', color = 'r')
ball_line2, = plt.plot([], [], '-', color = 'r')

plt.plot([0], [0], 'o', color = 'y', ms=20)

def animate(i):
  ball1.set_data(solve_func(i, 'point')[0])
  ball_line1.set_data(solve_func(i, 'line')[0])

  ball2.set_data(solve_func(i, 'point')[1])
  ball_line2.set_data(solve_func(i, 'line')[1])

ani = FuncAnimation(fig,
                    animate, 
                    frames=frames,
                    interval=30)

plt.axis('equal')
edge = 2*x10
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

plt.show()
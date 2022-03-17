import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 200
t = np.linspace(0, 15, frames) 

def move_function(z, t):
    x, x_0, y, v_y = z
    dxdt = x0
    dxx_dt = x_0
    dydt = v_y
    dv_ydt = y / (l * m) - g - (0.8 * m * v_y) + (5 * np.cos(W * t))
    return dxdt, dxx_dt, dydt, dv_ydt
  
v = 0.5
m = 0.5
Fy = 1
g = 9.98
l = -(8 * 10 ** (-2))
W = 1.5

x0 = 0
x_0_0 = 0
y0 = l
v_y0 = v

z0 =x0, x_0_0, y0, v_y0

def solve_func(i, key):
  sol = odeint(move_function, z0, t)
  if key == "point":
    x = sol[i, 0]
    y = sol[i, 2]
  else:
    x = sol[:i, 0]
    y = sol[:i, 2]
  return x, y

fig, ax = plt.subplots()
ball, = plt.plot([], [], "o", color = "g")
ball_line, = plt.plot([], [], "-", color = "g")

def animate(i):
  ball.set_data(solve_func(i, "point"))
  ball_line.set_data(solve_func(i, "line"))

ani = FuncAnimation(fig,
                   animate,
                   frames=frames,
                   interval = 30)

edge = 0.8
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, 0)

plt.show()
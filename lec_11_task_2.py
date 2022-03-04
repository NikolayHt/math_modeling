import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

frames = 200
t = np.linspace(0, 5, frames)

def move_func(z, t):
  x, y = z
  dxdt = u_x
  dydt = u_y
  return dxdt, dydt

g = 9.8
u = 20
k = 2
m = 0.5
alf = 50 * np.pi / 180
x0 = 0
u_x0 = u * np.cos(alf)
y0 = 0
u_y0 = u * np.sin(alf)
z0 = x0, u_x0, y0, u_y0



plt.show()
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 200
t = np.linspace(0, 50, frames) 

def move_function(z, t):
  x, y = z
  dxdt = (m - x - y) * k1
  dydt = (m - x - y) * k2
  return dxdt, dydt

m = 10
k1 = 0.2
k2 = 0.5
x0 = 0
y0 = 0

z0 = x0, y0

sol = odeint(move_function, z0, t)

plt.plot(t, sol[:, 1], "r", label="y(x)")
plt.plot(t, sol[:, 0], "b", label="z(x)")
plt.legend()
plt.show()
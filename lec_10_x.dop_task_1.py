import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-1, 1, 0.01)

def diff_func(k, t):
  x, y, z = k
  dxdt = 3 * x - y + z
  dydt = x + y + z
  dzdt = 4 * x - y + 4 * z
  return dxdt, dydt, dzdt

x0 = -71
y0 = 1
z0 = -3
k0 = x0, y0, z0

sol = odeint(diff_func, k0, t)

plt.plot(t, sol[:, 0], "b", label = "x(t)")
plt.plot(t, sol[:, 1], 'r', label = "y(t)") 
plt.plot(t, sol[:, 2], 'g', label = "z(t)") 
plt.legend()
plt.show()

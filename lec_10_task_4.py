import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.01)

def diff_func(z, t):
  w, y = z
  dydt = w
  dwdt = -4 * w - 5 * y
  return dydt, dwdt

y0 = 4
w0 = -1
z0 = w0, y0

sol = odeint(diff_func, z0, x)

plt.plot(x, sol[:, 1], "b", label = "x(t)")
plt.plot(x, sol[:, 0], 'r', label = "y(t)") 
plt.legend()
plt.show()
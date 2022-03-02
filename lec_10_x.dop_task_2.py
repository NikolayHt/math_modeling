import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(0.1, 5, 0.01)

def diff_func(k, x):
  y, w = k
  dydx = w
  dwdx = (w ** 2 - ((3*y**2)/np.sqrt(x)))/y
  return dydx, dwdx

y0 = 0.01
w0 = 1
k0 = y0, w0
sol = odeint(diff_func, k0, x)

plt.plot(x, sol[:, 1], "b", label = "x(t)")
plt.plot(x, sol[:, 0], 'r', label = "y(t)")
plt.legend()
plt.show()
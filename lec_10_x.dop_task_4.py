import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-1, 1, 0.01)

def diff_func(k, x):
  y, w = k
  dydx = w
  dwdx = -((x*w-(4*x**2+0.5)*y)/x**2)
  return dydx, dwdx

y0 = 3
w0 = 0
k0 = y0, w0
sol = odeint(diff_func, k0, x)

plt.plot(x, sol[:, 1], "b", label = "x(t)")
plt.plot(x, sol[:, 0], 'r', label = "y(t)")
plt.legend()
plt.show()
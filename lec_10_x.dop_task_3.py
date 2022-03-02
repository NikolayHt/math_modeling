import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 3, 0.01)

def diff_func(k, t):
  y, w = k
  dydt = w
  dwdt = np.sqrt(1 - w ** 2)
  return dydt, dwdt

y0 = 1
w0 = 0
k0 = y0, w0
sol = odeint(diff_func, k0, t)

plt.plot(t, sol[:, 1], "b", label = "x(t)")
plt.plot(t, sol[:, 0], 'r', label = "y(t)")
plt.legend()
plt.show()
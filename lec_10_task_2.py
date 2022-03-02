import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange (-1, 1, 0.01)

def diff_func(k, t):
  x, y = k
  dxdt = 3 * x - 2 * y + (np.e**(3*t)/np.e**t + 1)
  dydt = x - (np.e**(3*t)/np.e**t + 1)
  return dxdt, dydt

x0 = 5
y0 = -7
k0 = x0, y0

sol = odeint(diff_func, k0, t)

plt.plot(t, sol[:, 1], 'b', label = "x(t)")
plt.plot(t, sol[:, 0], 'r', label = "y(t)")        
plt.legend()
plt.show()




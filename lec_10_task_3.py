import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.01)

def diff_func(z, x):
    w, y = z
    dydt = w
    dwdt = np.sin(x) + np.cos(x)
    return dydt, dwdt

y0 = 3
w0 = 0
z0 = w0, y0

sol = odeint(diff_func, z0, x)

plt.plot(x, sol[:, 1], "b", label = "x(t)")
plt.plot(x, sol[:, 0], 'r', label = "y(t)") 
plt.legend()
plt.show()
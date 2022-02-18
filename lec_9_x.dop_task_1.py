import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


t = np.arange(0, 100, 0.01)

def radio_fun(v, t):
  dvdt = m * v * h
  return dvdt

v_0 = 10
m = 5
h = 100

solve = odeint(radio_fun, v_0, t)

plt.plot(t, solve[:,0])
plt.show()
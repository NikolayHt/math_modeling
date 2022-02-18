import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#УСКОРЕНИЕ ЛОКОМОТИВА

t = np.arange(0, 100, 0.01)

def radio_fun(v, t):
  F = b - k*v
  dvdt = F/m
  return dvdt

v_0 = 0
b = 1
k = 2
m = 10
solve = odeint(radio_fun, v_0, t)

plt.plot(t, solve[:,0])
plt.show()
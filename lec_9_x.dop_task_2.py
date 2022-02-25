import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(1, 24, 0.1)

def radio_function(S, t):
  dsdt = k * np.sqrt(S / np.pi) * E * S * np.cos(np.pi / 12 * (t - 12))       
  return dsdt
S_0 = 16
E = 1365.4
k = 340 * 10 ** (-8)
solve= odeint(radio_function, S_0, t)

plt.plot(t, solve[:, 0])
plt.show()
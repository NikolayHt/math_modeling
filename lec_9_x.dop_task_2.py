import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 24, 0.1)


def radio_function(S, t):
  dsdt = 2*r*np.sqrt(np.pi*S*r*S*np.cos(np.pi-(t-12)/t))
  return dsdt
S_0 = 1600
r = 1365,4
solve= odeint(radio_function, S_0, t)

plt.plot(t, solve[:, 0])
plt.show()




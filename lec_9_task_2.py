import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#ИНВЕСТИЦИИ

t = np.arange(0, 10, 1)

def radio_fun(e, t):
  dedt = -k * e * t
  return dedt

e_0 = 1000
k = 0.08
solve = odeint(radio_fun, e_0, t)

plt.plot(t, solve[:,0])
plt.show()
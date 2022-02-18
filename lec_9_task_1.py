import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#РАЗМНОЖЕНИЕ БАКТЕРИЙ

t = np.arange(0, 5, 0.01)

def radio_fun(N, t):
  dNdt = k * N
  return dNdt

N_0 = 10
k = 5
solve = odeint(radio_fun, N_0, t)

plt.plot(t, solve[:,0])
plt.show()
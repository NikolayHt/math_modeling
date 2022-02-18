import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#ДВИЖЕНИЕ МАТ. ТОЧКИ

t = np.arange(0, 5, 0.01)

def radio_fun(v, t):
  dvdt = F / m - gamma * v ** 2/ m 
  return dvdt

v_0 = 10
m = 5
F = 1
gamma = 0.1

solve = odeint(radio_fun, v_0, t)

plt.plot(t, solve[:,0])
plt.show()





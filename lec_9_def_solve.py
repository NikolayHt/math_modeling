import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 10**6, 100)

def radio_fun(m, t):
  dmdt = -k * m
  return dmdt

m_0 = 10
k = 1.61*10**(-6)#ПОСТОЯННАЯ РАСПАДА ДЛЯ ВИСМУТА 210
solve_Bi = odeint(radio_fun, m_0, t)

plt.plot(t, solve_Bi[:,0], label = "распад")
plt.show()
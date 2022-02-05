import matplotlib.pyplot as plt
import numpy as np

f='Циклоида(z) или астроида(a)'

def graf(f,R):
  if f == 'z':
    t = np.arange (-2*np.pi, 2*np.pi, 0.01)
    x = R*(t-(np.sin(t)**3))
    y = R*(1-(np.cos(t)**3))
  elif f == 'a':
    t = np.arange (-2*np.pi, 2*np.pi, 0.01)
    x = R*np.cos(t)**3
    y = R*np.sin(t)**3
  plt.plot(x, y, ls='--', lw=3)
  plt.axis('equal')
  plt.show()
print(graf(f='a',R=3))


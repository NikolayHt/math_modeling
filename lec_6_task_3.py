import matplotlib.pyplot as plt
import numpy as np
f='Окружность(o) или эллипс(e)'

def graf(f,rad=5,xa=-5,xb=5,N=0.01,a=3,b=4):
  x = np.arange(xa,xb,N)
  y = np.arange(xa,xb,N)
  X, Y = np.meshgrid(x,y)

  if f == 'o':
    fxy = X**2 + Y**2 - rad
    plt.title('Окружность') 
    plt.axis('equal')
  elif f == 'e':
    fxy = X**2 / a**2 + Y**2 / b**2 - rad
    plt.title('Эллипс')
    plt.axis('equal')
  plt.show()

graf(f='e')



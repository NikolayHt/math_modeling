import matplotlib.pyplot as plt
import numpy as np
f='Окружность(o) или эллипс(e)'

def graf(f,rad=10,xa=-2,xb=2,N=0.01,a=5,b=4):
  x = np.linspace(xa,xb,N)
  y = np.linspace(xa,xb,N)
  X, Y = np.meshgrid(x,y)
  if f == 'o':
    fxy = X**2 + Y**2
    plt.title('Окружность')
    plt.axis('equal')
  elif f == 'e':
    fxy = X**2 / a**2 + Y**2 / b**2 - 1
    plt.title('Эллипс')
  plt.contour(X,Y,fxy,levels=[0])
  plt.show()

graf(f='o')


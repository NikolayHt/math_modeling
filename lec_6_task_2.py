import matplotlib.pyplot as plt
import numpy as np
f='Парабола(p) или гипербола(g)'

def graf(f,a=1,b=3,c=6,k=1,xa=-100,xb=100,N=5):
  x = np.arange(xa,xb,N)
  if f == 'p':
    y=a*x**2+b*x+c
    plt.title('Парабола')
  elif f == 'g':
    y = k/x
    plt.title('Гипербола')
  plt.plot(x,y)
  plt.show()
graf(f='p')

import numpy as np 
a = np.zeros(4) 
a[0]=4
a[1]=8
a[2]=12
a[3]=16

def task(a):
  z = len(a)
  zz = 0
  for i in range (z):
    zz += a[i]
  print (zz/z)

task(a)

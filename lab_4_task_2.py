import numpy as np
a = np.zeros(3)
a[0]=4
a[1]=8
a[2]=12

def task(a):
  b = len(a)
  bb = 1
  for i in range (b):
    b *= a[i]
  print(bb/b)

task(a)   
 
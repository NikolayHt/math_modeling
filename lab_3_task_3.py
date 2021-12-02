from lab_3_task_1 import g
import numpy as np
x0 = 2
y0 = 3
V0 = 4
t = np.linspace(0,5)
x = x0 + V0*t
y = y0 + V0*t - (g*(t**2))/2
A = np.zeros((5,3))
for i in range(5):
  A[i,0]=t[i]
  A[i,1]=x[i]
  A[i,2]=y[i]
print(A)
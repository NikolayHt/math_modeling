import numpy as np
g = 9.82
a = np.zeros(3) #Масса тела; Высота полета; Скорость
for i in range(3):
  a[i] = int(input())

def task(a):
  E = a[0]*(a[2]**2)/2 + a[0]*g*a[1]
  print(E)

task(a)


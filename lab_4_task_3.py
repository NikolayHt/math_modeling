import numpy as np
g = 9.82
a = np.zeros(3) #Масса тела; Высота полета; Скорость
for i in range(3):
  a[i] = int(input())

def task(a):
  E = a[0] * a[1] * g
  print(E)

task(a)
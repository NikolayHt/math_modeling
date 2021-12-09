import numpy as np 
a = np.zeros((2,2))
b = np.zeros((2,2))
c = np.zeros((2,2))
for i in range(0, 2):
  for j in range(0, 2):
    a[i, j] = int(input('Первый массив = '))
print(a)  
for i in range(0, 2):
  for j in range(0, 2):
    b[i, j] = int(input('Второй массив =  '))
print(b)
print('Итог: ')
for i in range(0, 2):
  for j in range(0, 2):
    if a[i, j] > b[i, j]:
      c[i, j] = a[i, j]
    else:
      c[i, j] = b[i, j]
print(c)
import numpy as np 
M = 2
N = 3
a = np.zeros((2,3))
b = np.zeros((2,3))
c = np.zeros((2,3))
for i in range(N):
  for j in range(M):
    z = int(float(input('Первый массив =  ')))
    a = z
for i in range(N):
  for j in range(M):
    x = int(float(input('Второй массив =  ')))
    b = x
for i in range(N):
  for j in range(M):
    if a[i][j] > b[i][j]:
      c[i][j] = a[i][j]
    else: 
     c[i][j] = b[i][j]
print(a)
print(b)
print(c)




    
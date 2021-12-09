import numpy as np
a = np.zeros((5))
b = np.zeros((5))
c = np.zeros((5))
for i in range(5):
  a[i] = int(input('Данные массива one = '))
for i in range(5):
  b[i] = int(input('Данные массива two = '))
print(a)
print(b)
print('Итог: ')
for i in range(5):
  for j in range(5):
    if a[i] > b[i]:
      c[i] = a[i]
    else:
      c[i] = b[i]
print(c)
x = int(input('Укажите число: '))
 
for i in range(x):
  s = 1
  for y in range(2, i):
    if i % y == 0:
      s += y    
  if s == i:
    print(i)
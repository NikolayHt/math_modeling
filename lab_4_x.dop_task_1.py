def step(a,n):
  if n<0:
    a = 1/a
    n = -n
  b = 1
  while n>0:
    b = b * a
    n = n-1
    print(b)
step(2,5)
step(3,5)
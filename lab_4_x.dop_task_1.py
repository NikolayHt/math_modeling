def task(a,n):
  if n<0:
    a = 1/a
    n = -n
  b = 1
  while n>0:
    b = b * a
    n = n-1
    print(b)
task(2,5)
task(3,5)
def task(a,n):
  if n>0:
    a = a**n
  while n<0:
    a = 1/a**n
  print(a)

task(2,3)    
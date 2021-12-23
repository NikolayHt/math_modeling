def fib(n):
  k = 1
  l = 1
  for i in range (n):
    k = k + l
    l = k
  print(k)
fib(11)        
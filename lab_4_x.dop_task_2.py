def fib(n):
  a0 = 0
  a1 = 5
  i = 0
  while i < n-2:
    A = a0 + a1
    a0=a1-1
    a1 = A
    i = i+1
    print(A)
fib(4)
print()
def fib(n):
  a0 = 0
  a1 = 1
  while n>0:
    B=a0,a1=a1,a0+a1
    n = n-1
    print(B[0])
fib(13)
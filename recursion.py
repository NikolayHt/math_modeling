def fact(n):
  if 1 == n:
    return n 
  return n * fact(n-1)
print(fact(5))  


def fff(d, j):
  return d + j

lf = lambda d,j: d+j
print(fff, lf)
print(fff(4, 5), lf(4, 5))

import typing
def simulator(value: list, operation: typing.Callable):
  result = operation(value)
  return result

print(simulator([1, 4, 6], sum))
print(simulator([1, 4, 6], max))
print(simulator([1, 4, 6], lambda l: l[0] + l[2]))
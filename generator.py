"""k = [ x for x in range(10) if x%2 == 0]
   k = [ x for x in range(10) if not x%2]

k = []
for x in range (10):
  if x % 2 == 0:
    k.append(x)"""

"""dd = [x*y for x in range(10) for y in range(11, 20)]
print(dd, type(dd[0]))
"""
#generator
"""ge = (x**2 for x in range(10))
print(ge)
for f in ge:
  print(f)"""

#generator function
def func_gen(arg):
  x = 0
  while x < arg:
    kk = yield x**2
    print(kk)
    x += 1
gen = func_gen(4)    
print(next(gen))   
gen.send('Hello')
print(next(gen))  
print(next(gen))  

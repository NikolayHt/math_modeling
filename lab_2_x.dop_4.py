x = int(input("Bведите натуральное число = "))
b = 1
while x >= b:
  b += 1
  i = 2
  while i < b:

    if b % i == 0:
      b += 1
      i = 2
      
    i += 1
  while x % b == 0:
    x = x // b
    print(b)
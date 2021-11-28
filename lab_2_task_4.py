print("Ряд Фибоначчи")
a = 1
b = 1
n = int(input("Bведите число: "))
s = 0
print(a)
while s < n:
  print(b)
  c = a + b
  a = b
  b = c
  s += 1
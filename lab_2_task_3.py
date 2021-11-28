print("Определение года по високосности")
x = int(input("Введите год: "))
if x % 400 ==0:
  print("Високосный year")
elif x % 100 == 0:
  print("Невискосный year")
elif x % 4 == 0:
  print("Високосный year")
else:
  print("Невисокосный year")
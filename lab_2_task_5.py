print("Делитель числа")
a = float(input("Введите целое число: "))
b = float(input("Bведите целое число: "))
if b != 0:
  c = a / b
  print("Получилось => ", c)
  d = c % 1
  print("Остаток => ", d)
else:
  print("UNREAL")
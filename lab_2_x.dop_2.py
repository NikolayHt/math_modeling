print("Определение вида треугольника")
a = float(input('Длина первого отрезка: '))
b = float(input('Длина второго отрезка: '))
c = float(input('Длина третьего отрезка: '))
if a == b and b == c and a == c:
  print('Равносторонний')
elif a == b or b == c or a == c: 
  print('Равнобедеренный')
elif a != b and a != c and b != c:
  print('Разносторонний')
else:
  print('Треугольник не существует')
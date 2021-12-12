print("Программа для вычисления площади круга, квадрата, треугольника")
import numpy as np

def taskR(r):
  Sr = (r ** 2) * np.pi
  print("Площадь круга = ", Sr)
  return(Sr)

def taskSq(x):
  Ssq = x ** 2
  print("Площадь квадрата = ", Ssq)
  return(Ssq)

def taskTr(a, b, c):
  p = (a + b + c) / 2
  Str = (p*(p - a) * (p - b) * (p - c)) ** 0.5
  print("Площадь треугольника = ", Str)
  return(Str)

print('1 - круг, 2 - квадрат, 3 -треугольник')

ch = int(input())

if ch == 1:
  r = int(input("Радиус = "))
  taskR(r)
elif ch == 2:
  x = int(input("Сторона = "))
  taskSq(x)
elif ch == 3:
  a = int(input("a = "))
  b = int(input("b = "))
  c = int(input("c = "))
  taskTr(a, b, c)
  
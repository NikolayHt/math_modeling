print("Решение квадратного уранения")
a = float(input("Bведите кофициент а = "))
b = float(input("Bведите кофициент b = "))
c = float(input("Bведите кофициент с = "))

if a != 0:
  if b == 0 and c == 0:
    print("ONE корень")
    print(f'x = {0}') 
  elif b != 0 and c != 0:
    d = b ** 2 - 4*a*c
    print(f'd = {d}')
    
    if d < 0:
      print("NOT корней")
    elif d == 0:
        print("ONE корень")
        x = -b / (2*a)
        print(f'x=, {x}')
    else:
        print("TWO корней") 
        x1 = ((-b + d ** 0.5) / 2*a)
        x2 = ((-b - d ** 0.5) / 2*a)
        print(f'x1= {x1} x2= {x2}')  
elif b == 0:
  print("Неполное квадратное уравнение") 
  if -c / a < 0:
      print("NOT корней")
  elif -c/ a > 0:
      print("TWO корня")
      x1 = (-c / a)
      x2 = -x1
      print("x1 = ", x1, "x2 = ", x2) 
  else:    
      print("TWO корня")
      x1 = 0
      x2 = -b / a
      print(f'x1 = {x1} x2 = {x2}')
else:
  print("UNREAL")    
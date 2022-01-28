import matplotlib.pyplot as plt
import numpy as np
x = input("x=")
a = input("a=")
b = input("b=")

def grf(x, a, b):
  y = []
  for i in range (len()):
    if x[i] < a:
     y.append (a**2)
    if x[i] >= a and x[i] <= b:
     y.append (x[i]**2)
    if x[i] > b:
     y.append (b**2)  
  return x, y
plt.show()
grf()

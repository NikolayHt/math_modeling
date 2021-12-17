x0 = 10 #переменная в глобальной области
def move (t):
  x = x0 * t
  return x
print (move(3))  
#print (x) #name 'x' is not defined #локальная область

a = 'Good'

def my_func():
  a = 'Bad'
  print (a)
  
my_func()
print(a)  

class Valera:
  age = 88
  def cry(self):
    print("aaaAAAAaaaaaAAAaaaAA")
    
class Valera_two(Valera):
  def cry(self):
    print("EEEEEeEeeeEeEEee")
  

def main():
  ass = Valera_two()
  ass.cry()
  ass.age = 100
  print(ass.age)

if __name__ == '__main__':
  main()


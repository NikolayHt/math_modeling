class Fractal:
  def __init__(self):
    self.deep = 9
    self._size = 8
    self.__age = 15

def main():
  f = Fractal()
  print(f.deep)
  print(f._Fractal__age)

if __name__ == '__main__':
  main()
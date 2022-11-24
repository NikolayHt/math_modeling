class DictD(dict):
  def __init__(self, *k, **kw):
    self.__dict = dict(*k, **kw)
  def __setitem__(self, key, value):
    self.__dict.__setitem__(key, value)
  def __getitem__(self, item):
    if item in self.__dict:
      return self.__dict[item]
    else:
      return "Empty"
    
  

def main():
  d = DictD({"key": 77})
  print(d['key'])

if __name__ == '__main__':
  main()


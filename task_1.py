lang_1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
lang_2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}

class Alphabet:
  def __init__(self, long_0, count_0):
    self.long = long_0
    self.count = count_0
    
  def prt_all(self, count_0):
    print(count_0)

  def long_all(self, count_0):
    kol = len(count_0)
    print(kol)

a = Alphabet(1, lang_1)
a.prt_all(lang_1)
a.long_all(lang_1)
a.prt_all(lang_2)
a.long_all(lang_2)
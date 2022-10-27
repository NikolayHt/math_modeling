import random
states = ['отсутствует', 'цветение', 'опыление', 'зеленый', 'красный']

TOMATO_RIPED = 0
TOMATO_READY = len(states)-1


class WrongTomatoState(Exception):
  pass


def get_state_str(state):
  if state > 0 and state <= TOMATO_READY:
    return states[state]
  else:
    raise WrongTomatoState

spra = 'садоводство это весело и прикольно, садишь томаты, балдеешь на свежем воздухе, сказка!!!'


class Tomato:
  start_index = 0
  def  __init__(self):
    self.index = Tomato.start_index
    self.state = 1
    Tomato.start_index+=1
  def grow(self):
    print(self,' > ', end='')
    if self.state < TOMATO_READY:
      self.state += random.randint(0, 1)
    print(self)
  def is_ripe(self):
    return (self.state == TOMATO_READY)
  def __str__(self):
    return f'{self.__class__.__name__}, idx:{self.index}, state:{self.state}'
      

class TomatoBush:
  start_index_b = 0
  def  __init__(self, tomatos_count: int):
    self.tomatos = []
    self.index_b = TomatoBush.start_index_b
    TomatoBush.start_index_b += 1
    for _ in range(tomatos_count):
      self.tomatos.append(Tomato())
  def grow_all(self):
    for tomato in self.tomatos:
      tomato.grow()
  def all_are_ripe(self):
    check = True
    for tomato in self.tomatos:
      if not tomato.is_ripe():
        check = False
    print(f"all_are_ripe: {self} result = {check}")
    
    return check
  def give_away_all(self):
    if self.all_are_ripe() and len(self.tomatos):
      self.tomatos.clear()
      #print(f'дело сделано, для куста номер {self}')
  def __str__(self):
    return f'{self.__class__.__name__}, idx:{self.index_b}, tomatos count:{len(self.tomatos)}'
    

class Gardener:
  def  __init__(self, name: str, bushes: list):
    self.bushes = bushes
    self.name = name
  def work(self):
    for bush in self.bushes:
      bush.grow_all()
  def harvest(self):
    for bush in self.bushes:
      bush.give_away_all()

  def check_all_bushes_ripe(self):
    for bush in self.bushes:
      if not bush.all_are_ripe():
        return False
    return True
    
        
  def knowledge_base(self):
    print(spra)

# ------------------------------------------

h = []
for _  in range(random.randint(1, 5)):
   h.append(TomatoBush(random.randint(1, 30)))

g = Gardener("Bob", h)
iter = 0


while not g.check_all_bushes_ripe():
  
  print(f'Iteration: {iter}')
  g.work()
  g.harvest()
  iter+=1
  print()


print('The end')
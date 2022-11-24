class HUMAN:
  def __init__(self, default_name, default_age, _security_money, _security_home):
    self.default_name = default_name
    self.default_age = default_age
    self._security_money = _security_money
    self._security_home = _security_home
    
  def info(self):
    print(self.default_name, self.default_age, self._security_money, self._security_home)
    return
    
  def make_deal(self):
    self._security_money = self._security_money - 1000000
    self._security_home += 1
    m.info()
    
  def earn_money(self):
    self._security_money = self._security_money + 10000
    m.buy_home()
    return self._security_money
    
  def buy_home(self):
    if self._security_money >= 1000000:
      m.make_deal()
      print('You buy home')
    else:
      print('NoT money')
      m.earn_money()

class HOME:
  def __init__(self, _area, _price):
    self._area = _area
    self._price = _price

  def final_price (self, _price):
    self._price = self._price * 0.05

class SmallHome(HOME):
  def __init__(self, _area, _price):
    super().__init__(_area, _price)

m = HUMAN('Valera', 20, 1, 0)
HOME(40, 1000000)
SmallHome(40, 1000000)
m.buy_home()
class Vector:
  def __init__(self, x=2, y=3, z=4):
    self.x = x
    self.y = y
    self.z = z

  def __abs__(self):
    len = (self.x**2 + self.y**2 + self.z**2)*0.5
    return len

  def __repr__(self):
    str = f'{self.__class__.__name__}: ({self.x}, {self.y}, {self.z})'
    return str

  def __add__ (self, other):
    x_new = self.x + other.x
    y_new = self.y + other.y
    z_new = self.z + other.z
    return  Vector(x_new, y_new, z_new)

  def __sub__ (self,other):
    x_new = self.x - other.x
    y_new = self.y - other.y
    z_new = self.z - other.z
    return  Vector(x_new, y_new, z_new)

  def __mul__ (self, other):
    if isinstance(other, Vector):
      a = Vector((self.y * other.z) - (self.z * other.y), (self.z * other.x) - (self.x * other.z), (self.x * other.y) - (self.y * other.x) )
      return a
    else:
      a = Vector (self.x * other, self.y * other, self.z * other)
      return a

  def __eq__(self, other):  
    if self.x == other.x and self.y == other.y and self.z == other.z:
      return True
    else:
      return False

  def __pow__(self, other):
    x1 = self.x**other
    y1 = self.y**other  
    z1 = self.z**other
    return Vector(x1, y1, z1)
    
v = Vector()
v1 = Vector()
v2 = Vector(0, 5, 0)
v3 = Vector(5, 0, 0)

print(v, abs(v), v-v1, v+v1)
print(v3*v2, v2*v3)
print(v3*4)
print(v == v1)
class ORGANIC_Cell:
    def __init__(self, volume=10, energy=100):
      self.volume = volume
      self.energy = energy

    def __mul__(self, other):
      volume_new = self.volume * other
      return[ORGANIC_Cell()]

    def __add__ (self, other):
      volume_new = self.volume + other
      return[ORGANIC_Cell()]
      
    def __sub__ (self, other):
      volume_new = self.volume - other
      return[ORGANIC_Cell()]
      
    def __truediv__ (self, other):
      volume_new = self.volume / other
      round(volume_new)
      return[ORGANIC_Cell()]

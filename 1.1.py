class StarSystem:
    def __init__(self, planets, name):
        self.planets = list(planets)
        self.name = name
        
    def __len__(self):
        return len(self.planets)
        
    def __add__(self, other):
        planets_1 = self.planets.copy()
        planets_1.append(other)
        return StarSystem(planets_1, self.name)
system = StarSystem(['planet1', 'planet2', 'planet3'], 'StarSystem1')
len(system)
system = system + 'planet4'
system.planets

class Number1:
    def __init__ (self, val):
        self.val = val
        
    def __add__ (self, other):
        print('add', self.val, other)
        return self.val + other


      
    # __radd__ = __add__
    
    def __radd__ (self, other):
        print (' radd ', self.val, other)
        return other + self.val
      	# return self.__add__(other)
      	# return self.val + other
x = Number1(32)
y = Number1(25)

x + 1
2 + y
x + y


class StarSystem:
    def __init__(self, planets, name):
        self.planets = list(planets)
        self.name = name
        
    def __add__(self, other):
        planets_1 = self.planets.copy()
        planets_1.append(other)
        return StarSystem(planets_1, self.name)
      
    def __radd__(self, other):
        planets_1 = self.planets.copy()
        planets_1.insert(0, other)
        return StarSystem(planets_1, self.name)
system_1 = StarSystem(['planet_1'], 'System_1')
system_1 = system_1 + 'planet_2'
system_1.planets

system_1 = 'planet_3' + system_1
system_1.planets


class StarSystem:
    def __init__(self, planets, name):
        self.planets = list(planets)
        self.name = name
        
    def __iadd__(self, other):
        self.planets.append(other)
        return self
      
system_1 = StarSystem(['planet_1'], 'System_1')
system_1 += 'planet_2'
system_1.planets

class StarSystem:
    def __init__(self, planets, name):
        self.planets = list(planets)
        self.name = name
        
    def __iadd__(self, other):
        self.planets.append(other)
        return self
      
system_1 = StarSystem(['planet_1'], 'System_1')
system_1 += 'planet_2'
system_1.planets

class StarSystem:
    def __init__(self, planets, name):
        self.planets = list(planets)
        self.name = name
        
    def __str__(self):
        return f'Название системы {self.name} \
        и её планеты {[i for i in self.planets]}'


class StarSystem:
    def __init__(self, planets, name):
        self.planets = list(planets)
        self.name = name
        
    def __str__(self):
        return f'Название системы {self.name} \
        и её планеты {[i for i in self.planets]}'
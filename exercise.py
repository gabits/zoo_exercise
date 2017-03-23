


class Animal(object):
    def __init__(self):
        self.preys = []
            
class Lion(Animal):
    def __init__(self):
        self.name = "unnamed"
        self.preys = [Hyena, Wildebeest]
    
class Hyena(Animal):
    pass

class Snake(Animal):
    pass




class Zoo(Cages):
    def __init__(self):
        self.cages = cages

class Cage(object):
    def __init__(self):
        self.animals = []        

for animal in list_of_animals:
    for all_animals in list_of_animals: # For each instance of the list, check the preys and compare to the object type 
        if type(other_animals) in animal.preys:
            all_animals.eaten_by(animal)

class Animal(object):
    def __init__(self):
        self.preys = []
        self.alive = True
    def get_eaten(self, animal):
        self.alive = False
        self.eaten_by = animal
    
        
class Lion(Animal):
    def __init__(self):
        self.name = "unnamed"
        self.preys = [Hyena, Wildebeest]
    
class Hyena(Animal):
    pass

class Snake(Animal):
    pass




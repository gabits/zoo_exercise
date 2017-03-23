
class Animal(object):
    def __init__(self):
        self.name = 'unnamed'
        self.preys = []
    
class Snake(Animal):
    def __init__(self):
        self.preys = []
        self.name = 'unnamed'
        
class Falcon(Animal):
    def __init__(self):
        self.preys = [Snake]
    
class Racoon(Animal):
    def __init__(self):
        self.preys = [Snake]

class Cage(Animal):
    def __init__(self, name):
        self.name = name
        self.animals_list = []  
        self.dead_animals = []
    def add(self, *args):
        animal_death = False
        for animal in args:
            self.animals_list.append(animal)  
        for predator in self.animals_list:
            count = 0
            for prey in self.animals_list:
                if type(prey) in predator.preys:                    
                    print("Oops! Seems like you put predator and prey in the same cage.")
                    del self.animals_list[count]
                    self.dead_animals.append(prey)
                    print(prey.name + " (" + type(prey).__name__ + ") was eaten by "
                          + predator.name + " (" +  type(predator).__name__ + ")")
                    self.animal_death = True                
            count += 1
        print(self.animals_list)
        if animal_death:
            print(self.dead_animals)
        
               

class Zoo(Cage):
    def __init__(self, *args):
        cages = {}
        self.cages = cages
        if args > 0:
            for cage in args:
                cages[cage.name] = cage
    def n_of_cages(self):
        number = len(self.cages)
        return number

class Animal(object):
    def __init__(self):
        self.name = 'Unnamed'
        self.preys = []
        self.id = str(self.name) + " " + type(self).__name__

    
class Snake(Animal):
    def __init__(self):
        super(Snake, self).__init__()
        self.preys = []

        
class Falcon(Animal):
    def __init__(self):
        super(Falcon, self).__init__()
        self.preys = [Snake]

    
class Racoon(Animal):
    def __init__(self):
        super(Racoon, self).__init__()
        self.preys = [Snake]


class Coyote(Animal):
    def __init__(self):
        super(Coyote, self).__init__()
        self.preys = [Racoon]


class Lion(Animal):
    def __init__(self):
        super(Lion, self).__init__()
        self.preys = [Coyote]
        
        
class Cage(Animal):
    def __init__(self):
        self.animals = []
    def animals_inside(self):
        names_list = []
        if len(self.animals) > 0:
            for item in self.animals:
                names_list.append(item.id)
                print("Animals in this cage: {}".format(names_list))
        else:
            print('This cage is empty')
    def add_animals(self, *args):
        for animal in args:
            self.animals.append(animal) # Inserts Animal object in cage   
        for predator in self.animals:
            count = 0
            for prey in self.animals:
                if type(prey) in predator.preys:                    
                    print("Oops! Seems like you put predator and prey in the same cage.")
                    del self.animals[count]
                    print("{} was eaten by {}.".format(prey.id, predator.id))                
            count += 1
        self.animals_inside()


class Zoo(Cage):
    def __init__(self):
        super(Cage, self).__init__()
        self.cages = []
    def add_cage(self, *args):
        for cage in args:
            self.cages.append(cage)
    def n_of_cages(self):
        number = len(self.cages)
        return number

class Animal:
    """ Creates Animal object with a name and a list of preys. """

    def __init__(self):
        self.name = 'Unnamed'
        self.preys = []
        self.identification = str(self.name) + " " + type(self).__name__

    
class Snake(Animal):
    """ Creates Lion object inheriting attributes and methods from Animal class. """

    def __init__(self):
        super().__init__()
        self.preys = []

        
class Falcon(Animal):
    """ Creates Falcon object inheriting attributes and methods from Animal class. """

    def __init__(self):
        super().__init__()
        self.preys = [Snake]

    
class Racoon(Animal):
    """ Creates Racoon object inheriting attributes and methods from Animal class. """

    def __init__(self):
        super().__init__()
        self.preys = [Snake] # Defines


class Coyote(Animal):
    """ Creates Coyote object inheriting attributes and methods from Animal class. """

    def __init__(self):
        super().__init__()
        self.preys = [Racoon]


class Lion(Animal):
    """ Creates Lion object inheriting attributes and methods from Animal class. """

    def __init__(self):
        super().__init__()
        self.preys = [Coyote]
        
        
class Cage(Zoo):
    """ Creates a Cage object, inheriting from Zoo class, with a list of animals inside. """

    def __init__(self):
        super().__init__()
        """Starts an object of Cage class with an empty list of animals"""
        self.animals = []
        ### self.zoo
        self.n_of_animals = len(self.animals) # Count of all alive animals inside the cage

    def __repr__(self):
        """Human friendly-readable format of Cage class representation"""
        if zoo for cage in zoo:
        return 'Cage{} contains {} animals: {}'.format(self.name, self.n_of_animals, self.animals)

    def animals_inside(self):
        names_list = []
        if len(self.animals) > 0:
            for item in self.animals:
                names_list.append(item.id)
                print("Animals in this cage: {}".format(names_list))
        else:
            print('This cage is empty')

    def add_animals(self, add_list):
        for animal in add_list:
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


class Zoo:
    """Creates Zoo object that can contain a list of Cage objects. """

    def __init__(self):
        self.cages = []

    def add_cage(self, *args):
        for cage in args:
            self.cages.append(cage)

    def n_of_cages(self):
        number = len(self.cages)
        return number

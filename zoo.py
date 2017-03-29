class Animal:
    """ Creates Animal object with a name and a list of preys. """

    def __init__(self):
        self.name = 'Unnamed' # Default naming, to be modified
        self.preys = []
    
    def __repr__(self):
        """ Representation of animal object identifying its name and species (subclass). """
        return str(self.name) + " " + type(self).__name__
            
    
class Snake(Animal):
    """ Creates Snake object inheriting attributes and methods from Animal class. """

    def __init__(self):
        super().__init__()
        self.preys = [] # List of Animal subclasses that Snakes eat

        
class Falcon(Animal):
    """ Creates Falcon object inheriting attributes and methods from Animal class. """

    def __init__(self):
        super().__init__()
        self.preys = [Snake] # List of Animal subclasses that Falcons eat
    
    
class Racoon(Animal):
    """ Creates Racoon object inheriting attributes and methods from Animal class. """

    def __init__(self):
        super().__init__()
        self.preys = [Snake] # List of Animal subclasses that Racoons eat


class Coyote(Animal):
    """ Creates Coyote object inheriting attributes and methods from Animal class. """

    def __init__(self):
        super().__init__()
        self.preys = [Racoon] # List of Animal subclasses that Coyotes eat 


class Lion(Animal):
    """ Creates Lion object inheriting attributes and methods from Animal class. """

    def __init__(self):
        super().__init__()
        self.preys = [Coyote] # List of Animal subclasses that Lions eat
        
        
class Cage:
    """ 
    Creates a Cage object, inheriting from Zoo class, 
    with a list of animals inside. """

    def __init__(self):
        """ Starts an object of Cage class with an empty list of animals. """
        self.animals_list = []
        self.n_of_animals = len(self.animals_list) # Count of all alive animals inside the cage
        self.name = 'Cage' # Default name configuration
        
    def __repr__(self):
        """ Human friendly-readable format of Cage class representation. """
        if len(self.animals_list) > 0:
            return "{} contains {} animals: {}".format(self.name, self.n_of_animals, self.animals)
        else:
            return "{} (empty)".format(self.name)

    def check_preys(self):
        """ 
        Method for checking the animals chain food competition inside a cage:
        Iterates through its animals list and kills (deletes) the predator's
        preys. """       
        # Iteration through each animal in the list to check if it has listed preys inside the cage:
        for predator in self.animals_list: # 
            prey_index = 0
            for prey in self.animals_list: # Iterates trough the animal's preys Class list
                """ Compares the listed classes in an animal's preys list 
                with the class of each other animal on the cage. """
                if type(prey) in predator.preys:                     
                    print("Oops! Seems like you put predator and prey in the same cage.")
                    del self.animals_list[prey_index] # Kills the prey: deletion by its index 
                    print("{} was eaten by {}.".format(prey, predator))                
                prey_index += 1 # Increases index number for iterator  

        print(self) # Prints updated list of animals inside the cage
    def add_animals(self, add_list):
        """ Method that allows you to insert animals inside the Cage object. """
        for animal in add_list:
            self.animals_list.append(animal) # Inserts Animal object in cage   
        check_preys(self.animals_list) 
        # Will perform a check on whether there is prey and predator on the same cage
    
        
class Zoo(Cage):
    """ Creates Zoo object that can contain a list of Cage objects. """

    
    def __init__(self):
        super().__init__()
        self.name = 'Zoo' # Default name  
        self.cages = []
        self.n_of_cages = len(self.cages)

    def __repr__(self):
        self.n_of_animals = sum(item.n_of_animals for item in self.cages)
        """ Human friendly-readable format of Zoo class representation. """
        if self.n_of_cages > 0:
            return '{} contains {} cages and a total of {} animals'.format(self.name, self.n_of_cages, self.n_of_animals)
        else:
            return '{} (empty)'.format(self.name)
    
    def add_cage(self, list_to_add):
        for cage in list_to_add:
            self.cages.append(cage)
        return self
class Animal:
    """ Creates Animal object with a name and a list of preys. """

    def __init__(self):
        self.name = 'Unnamed' # Default naming, to be modified
        self.preys = []
    
    def __repr__(self):
        """ Representation of animal object identifying its name and species (subclass). """
        return str(self.name) + " " + type(self).__name__
            
    
class Goat(Animal):
    """ Creates Goat object inheriting attributes and methods from Animal class. """

    def __init__(self):
        super().__init__()
        self.preys = [] # List of Animal subclasses that Goats eat

        
class Jackal(Animal):
    """ Creates Jackal object inheriting attributes and methods from Animal class. """

    def __init__(self):
        super().__init__()
        self.preys = [Goat, Rabbit] # List of Animal subclasses that Jackals eat
    
    
class Rabbit(Animal):
    """ Creates Rabbit object inheriting attributes and methods from Animal class. """

    def __init__(self):
        super().__init__()
        self.preys = [Mouse] # List of Animal subclasses that Rabbits eat


class Owl(Animal):
    """ Creates Owl object inheriting attributes and methods from Animal class. """

    def __init__(self):
        super().__init__()
        self.preys = [Mouse] # List of Animal subclasses that Owls eat 


class Mouse(Animal):
    """ Creates Mouse object inheriting attributes and methods from Animal class. """

    def __init__(self):
        super().__init__()
        self.preys = [] # List of Animal subclasses that Mouses eat


class Snake(Animal):
    """ Creates Snake object inheriting attributes and methods from Animal class. """

    def __init__(self):
        super().__init__()
        self.preys = [Mouse] # List of Animal subclasses that Snakes eat
     
     
class Kite(Animal):
    """ Creates Kite object inheriting attributes and methods from Animal class. """

    def __init__(self):
        super().__init__()
        self.preys = [Snake] # List of Animal subclasses that Kites eat
             
        
class WildCat(Animal):
    """ Creates WildCat object inheriting attributes and methods from Animal class. """

    def __init__(self):
        super().__init__()
        self.preys = [Rabbit, Mouse] # List of Animal subclasses that WildCats eat
     
             
class Lion(Animal):
    """ Creates Lion object inheriting attributes and methods from Animal class. """

    def __init__(self):
        super().__init__()
        self.preys = [Goat, Jackal, WildCat, Kite] # List of Animal subclasses that Lions eat
             
        
        
class Cage:
    """ 
    Creates a Cage object, inheriting from Zoo class, 
    with a list of animals inside. """

    def __init__(self):
        """ Starts an object of Cage class with an empty list of animals. """
        self.animals_list = []
        self.name = 'Cage' # Default name configuration
        
    def __repr__(self):
        """ Human friendly-readable format of Cage class representation. """
        if len(self.animals_list) > 0: # Checks if cage isn't empty
            return "{} contains {} animals: {}".format(self.name, len(self.animals_list), self.animals_list)
        else:
            return "{} (empty)".format(self.name)

    def check_preys(self):
        """ 
        Method for checking the animals chain food competition inside a cage:
        Iterates through its animals list and kills (deletes) the predator's
        preys. """       
        # Iteration through each animal in the list to check if it has listed preys inside the cage:
        death_statements = []
        for predator in self.animals_list:
            prey_index = 0
            for prey in self.animals_list: # Iterates trough the animal's preys Class list
                """ Compares the listed classes in an animal's preys list 
                with the class of each other animal on the cage. """
                if type(prey) in predator.preys:                     
                    del self.animals_list[prey_index] # Kills the prey: deletion by its index 
                    death_statements.append("{} got eaten by {}.".format(prey, predator))                
                prey_index += 1 # Increases index number for iterator  
        if len(death_statements) > 0 :
             print("Oops! Seems like you put predator and prey in the same cage.")
             for statement in death_statements:
                 print(statement)
        print('Now ' + str(self)) # Prints updated list of animals inside the cage

    def add_animals(self, add_list):
        """ Method that allows you to insert animals inside the Cage object. """
        duplicate_animals = []
        for animal in add_list:
            if animal not in self.animals_list:
                # Will insert Animal object in cage if they're not already inside    
                self.animals_list.append(animal)
            else:
                if animal not in duplicate_animals:
                    duplicate_animals.append(animal) 
        if len(duplicate_animals) > 0:
            duplicates = str(duplicate_animals[0])
            if len(duplicate_animals) > 1 :
                for animal in duplicate_animals[1:]:
                    duplicates += (', ' + str(animal)) 
            print("You can't put the same animal in a cage more than once: {} already inside.".format(
                duplicates))
            print(self)
        return self.check_preys()
        # Will perform a check on whether there is prey and predator on the same cage
    
        
class Zoo(Cage):
    """ 
    Creates Zoo object that can contain a list of Cage objects. 
    Inherits from Cage to access the Animal objects in each. """
    
    def __init__(self):
        super().__init__()
        self.name = 'Zoo' # Default name  
        self.cages = []

    def __repr__(self):
        """ Human friendly-readable format of Zoo class representation. """
        self.n_of_cages = len(self.cages) # Calculates the number of cages inside the zoo
        if self.n_of_cages > 0:
            return '{} contains {} cages and a total of {} animals'.format(
                self.name, self.n_of_cages, self.animals_count())
        else:
            return '{} (empty)'.format(self.name)
    
    def add_cage(self, list_to_add): # Adds each Cage instances inside a given list as argument
        for cage in list_to_add: 
            self.cages.append(cage)
        return self

    def animals_count(self):
        """ 
        Acessing attributes from instances of class Cage, it calculates how many
        animals are in total inside all cages of the zoo. """
        self.n_of_animals = 0
        for item in self.cages: 
            # Appends to attribute sum of animals inside each cage
            self.n_of_animals += len(item.animals_list) 
        return self.n_of_animals
class Animal:
    """ Can be placed inside cages, and according to its place in food chain
    it has a list attribute of its prey (what it likes to eat). 
    """

    def __init__(self):
        self.name = 'Unnamed' # Default naming, to be modified
        self.prey = []
    
    def __repr__(self):
        """ Identifies the Animal by its name and species (subclass). 
        """
        return str(self.name) + " " + type(self).__name__
            
    
class Goat(Animal):

    def __init__(self):
        super().__init__()

        
class Jackal(Animal):

    self.prey = [Goat, Rabbit] # List of Animal subclasses that Jackals eat

    def __init__(self):
        super().__init__()
    
    
class Rabbit(Animal):

    self.prey = [Mouse] # List of Animal subclasses that Rabbits eat
    
    def __init__(self):
        super().__init__()


class Owl(Animal):

    self.prey = [Mouse] # List of Animal subclasses that Owls eat 
    
    def __init__(self):
        super().__init__()


class Mouse(Animal):

    def __init__(self):
        super().__init__()


class Snake(Animal):

    self.prey = [Mouse] # List of Animal subclasses that Snakes eat
    
    def __init__(self):
        super().__init__()
    
     
class Kite(Animal):

    self.prey = [Snake] # List of Animal subclasses that Kites eat
    
    def __init__(self):
        super().__init__()
             
        
class WildCat(Animal):
    
    self.prey = [Rabbit, Mouse] # List of Animal subclasses that WildCats eat

    def __init__(self):
        super().__init__()
     
             
class Lion(Animal):

    self.prey = [Goat, Jackal, WildCat, Kite] # List of Animal subclasses that Lions eat
    
    def __init__(self):
        super().__init__()
              
        
class Cage:
    """ Contains a list of animals inside and performs methods to check the 
    intern competition where there might be a conflict of prey and predator.  
    """

    def __init__(self):
        self.animals_list = []
        self.name = 'Cage' # Default name configuration
        
    def __repr__(self):
        if len(self.animals_list) > 0: # Checks if cage isn't empty
            return "{} contains {} animals: {}".format(self.name, len(self.animals_list), self.animals_list)
        else:
            return "{} (empty)".format(self.name)

    def check_prey(self):
        """ Method for checking the animals chain food competition inside a 
        cage: iterates through its animals list and kills (deletes) the 
        predator's prey. 
        """       
        death_statements = []
        # Iteration through each animal in the list to check if it has listed prey inside the cage:
        for predator in self.animals_list:
            prey_index = 0
            for prey in self.animals_list: # Iterates trough the animal's prey Class list
                """ Compares the listed classes in an animal's prey list 
                with the class of each other animal on the cage. """
                if type(prey) in predator.prey:                     
                    del self.animals_list[prey_index] # Kills the prey: deletion by its index 
                    death_statements.append("{} got eaten by {}.".format(prey, predator))                
                prey_index += 1 # Increases index number for iterator  
        if len(death_statements) > 0 :
             print("Oops! Seems like you put predator and prey in the same cage.")
             for statement in death_statements:
                 print(statement)
        print('Now ' + str(self)) # Prints updated list of animals inside the cage

    def add_animals(self, add_list):
        """ Inserts animals inside the Cage object. 
        """
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
        return self.check_prey()
        # Will perform a check on whether there is prey and predator on the same cage
    
        
class Zoo:
    """ Contains a list of Cage objects and informs about the animals inside
    itself.
    """
    
    def __init__(self):
        super().__init__()
        self.name = 'Zoo' # Default name  
        self.cages = []

    def __repr__(self):
        """ Human friendly-readable format of Zoo class representation. 
        """
        self.n_of_cages = len(self.cages) # Calculates the number of cages inside the zoo
        if self.n_of_cages > 0:
            return '{} contains {} cages and a total of {} animals'.format(
                self.name, self.n_of_cages, self.animals_count())
        else:
            return '{} (empty)'.format(self.name)
    
    def add_cages(self, list_to_add): # Adds each Cage instances inside a given list as argument
        for cage in list_to_add: 
            self.cages.append(cage)
        return self

    def animals_count(self):
        """ Accessing attributes from instances of class Cage, it calculates 
        how many animals are in total inside all cages of the zoo. 
        """
        self.n_of_animals = 0
        for item in self.cages: 
            # Appends to attribute sum of animals inside each cage
            self.n_of_animals += len(item.animals_list) 
        return self.n_of_animals
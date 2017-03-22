>>> import zoo


>>> lion_1 = Lion('Leo', 4) """" Name = 'Leo', age = 4 """ # Problems: needs to create object according to class and append to dictionary
>>> Wildebeest('Joseph', 7)
>>> Hyena.place_in_food_chain
prey
>>> Hyena('Yara', 2)
>>> display_existing_animals() # Creates a dictionary for all Animal objects created by species subclasses
{ 'Leo': {'species': Lion, 'age': 4, 'place in food chain': 'predator', 'alive': True, 'cage': None}, 
                        # { animal.name: type_of(animal), 'age: ' + animal.age, Species.place_in_food_chain' }
                            'Joseph': {'species': Wildebeest, 'age': 7, 'place in food chain': 'prey', 'alive': False, 'eaten_by': Leo}}
                        # type_of(animal) is supposed to show the respective class of variable animal




# Zoo methods
>>> n_of_cages() # Prints number of cages (number of occurances in zoo dictionary)
>>> list_of_animals('Cage 1') # Argument given is taken as dictionary key for value containing cage list of animals 
[Leo, Joseph, Yara]
>>> dead_animals('Cage 1') # Iterates through 'Cage 1' list and returns all objects whose .alive attribute is False.
[Joseph, Yara]


cage_1.append()


# Attributes
>>> Leo.species # Prints class (type) of Leo
Lion 
>>> Leo.age
4
>>> Wildebeest.place_in_food_chain
prey
>>> Leo.alive
True
>>> Wildebeest.alive
False
>>> Wildebeest.eaten_by # Keeps track of alive attribute True objects in the same cage *
Leo
>>> Wildebeest.eaten_by.species
Lion


>>> Zoo['Cage 1'] = [ Leo, Joseph, Yara ]

class Zoo(Cages):
    def __init__(self):
        self.cages = cages

zoo = Zoo() # Creates empty Zoo

cage_1 = [] # Creates empty Cage
cage_2 = [lion_1, hyena_4, wildebeest_2]

>>> lion_1 = Lion() 
>>> cage_1.append(lion_1)
>>> cage_2.append(lion_2)



class Cage(object):
    def __init__(self):
        self.list_of_animals = []        



# 
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




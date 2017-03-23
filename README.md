>>> from zoo import Zoo, Cage, Animal, Lion, Hyena, Wildebeest, Snake # ...

# Create a Zoo
>>> london_zoo = Zoo()

# Create different cages
>>> cage_1 = Cage() # Empty cage
>>> london_zoo.cages = [cage_1, cage_7, cage_2, cage_5] # Populate Zoo with cages

# Find out how many cages are in the zoo
>>> len(london_zoo.cages)
4

# Place different animals (of particular species) in cages
>>> lion_1 = Lion()
>>> snake_3 = Snake()
>>> cage_1.animals = [lion_1, snake_3]

# Be able to name the animals 
>>> lion_2 = Lion('Leo')
>>> snake_1 = Snake('Flora')

# 5. List animals inside a cage
>>> cage_5.animals
[wildebeest_1, lion_3, snake_4] # This is attribute of class Cage returns a list

# Repopulating a cage
>>> del cage_5.animals[2]
>>> cage_5.animals
[wildebeest_1, lion_3]
>>> cage_5.add(rat_3, rat_5, hyena_2)
>>> cage_5.animals
[wildebeest_1, lion_3, rat_3, rat_5, hyena_2]

# Make preys get eaten by predators if in same cage
>>> cage_5.animals.add(snake_4)
"""Oops! Seems like you put predator and prey in the same cage.
Animals in the cage: [lion_3, hyena_2, snake_4]
Dead animals: [rat_3, rat_5]"""

# List which predator ate which prey
>>> cage_5.who_was_the_predator()
"""rat_3: eaten by snake_4
rat_5: eaten by snake_4"""
>>> cage_2.who_was_the_predator()
"""No animal has been eaten in this cage."""

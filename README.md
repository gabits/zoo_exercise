# Proposal

As an exercise to train the logic of Python classes and how objects behave with them, I was given this project proposal. Below the requirements for the code, there's a simple documentation and instructions for expected usages of the code in the command-line. 

## Zoo Game

You are a zoo keeper.  Write a command-line program in Python that simulates a simple zoo, using object oriented programming.  You should be able to do the following: 

* Create different cages in the zoo.  At any time, you should be able to find out how many cages are in the zoo.
* Put different animals in the cages. 
* Each animal should be of a particular species (e.g. 'Lion'), and have a name given to them by the zookeeper (e.g. 'Growler').
* Find out which animals are in a particular cage.
* Some species of animals like eating other species of animals.  For example, lions like eating wildebeest.  If you put prey and predator in the same cage, then all the prey should be eaten by the predator.  (The program should tell you which predator ate which prey by printing to the console.)



# Documentation
```
>>> from zoo import Zoo, Cage, Animal, Lion, Hyena, Wildebeest, Snake # ...
```

### Create a Zoo
```
>>> london_zoo = Zoo()
```

### Create different cages
```
>>> cage_1 = Cage() 
>>> london_zoo.cages = [cage_1, cage_7, cage_2, cage_5] # Populate Zoo with cages
```

### Find out how many cages are in the zoo
```
>>> london_zoo.n_of_cages()
4
```

### Place different animals (of particular species) in cages
```>>> lion_1 = Lion()
>>> snake_3 = Snake()
>>> cage_1.animals = [lion_1, snake_3]
>>> cage_2 = Cage(wildebeest_1, wildebeest_5)
```

### Be able to name the animals 
```
>>> lion_2.name = 'Leo'
>>> snake_1.name = 'Flora'
```

### List animals inside a cage
```
>>> cage_5.animals_inside()
# Does not return the Animal objects inside the cage, but a list of strings related to them as an ID attribute
Animals inside this cage: ['Unnamed Coyote', 'Flora Snake', 'Unnamed Snake'] 
>>> cage_6.animals_inside()
This cage is empty.
```

### Repopulating a cage
```
>>> del cage_5.animals[2]
>>> cage_5.animals_inside()
Animals inside this cage: ['Unnamed Coyote', 'Flora Snake']
>>> snake_3 = Snake()
>>> snake_5 = Snake()
>>> cage_5.add_animals(snake_3, snake_5)
>>> cage_5.animals_inside()
Animals in this cage: ['Unnamed Coyote', 'Flora Snake', 'Unnamed Snake', 'Unnamed Snake']
```

### Make preys get eaten by predators if in same cage
```
>>> cage_5.add_animals(coyote_3, lion_1)
Oops! Seems like you put predator and prey in the same cage.
Yves Coyote was eaten by Leo Lion.
Animals in this cage: ['Unnamed Falcon', 'Leo Lion']
```

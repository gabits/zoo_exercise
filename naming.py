from zoo import (Zoo, Cage, Animal, Mouse, WildCat, Lion, Owl, Goat, Jackal, 
                 Rabbit, Kite)

class AutoId(Animals, Cages, Zoo):
    
    # Method for naming = False (default options)
    # Method for naming = strings
    # Method for naming = integers
    # Create a test for Animal object generator
    
    self.animal_classes = [Mouse, WildCat, Lion, Owl, Goat, Jackal, Rabbit, Kite]

    def naming(self):    
        for i in range(20):
            random_list.add_animals([random.choice(self.animal_classes)()])       
        list_1 = list_name[:10]
        list_2 = list_name[10:]
        return list_1, list_2
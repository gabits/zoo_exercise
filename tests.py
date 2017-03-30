from zoo import Zoo, Cage, Animal, Mouse, WildCat, Lion, Owl, Goat, Jackal, Rabbit, Kite
from unittest import TestCase, main

class ZooScenario(TestCase):
    
    def create_objects(self):
            # Creation of zoo and cages:
        zoo = Zoo()
        cage_1 = Cage()
        cage_2 = Cage()
        cage_3 = Cage()        
            # Creation of animals:
        lion_1 = Lion()
        lion_2 = Lion()
        kite_1 = Kite()
        snake_1 = Snake()
        goat_1 = Goat()
        jackal_1 = Jackal()
        owl_1 = Owl()
        rabbit_1 = Rabbit()
        rabbit_2 = Rabbit()
        mouse_1 = Mouse()
        mouse_2 = Mouse()
        mouse_3 = Mouse()

        list_1 = [mouse_2, snake_1, goat_1, mouse_2, goat_1, mouse_2]
        list_2 = [lion_2, mouse_3, snake_1, jackal_1, rabbit_1, mouse_1]
        list_3 = [cage_1, cage_2, cage_3]
        
        check_contents()
        
        # self.assertTrue()
        
    def check_contents(self):
            # Tests zoo with empty cages
        zoo.add_cages(list_3)
        self.assertEqual(zoo.cages, [])
            # Tests multiple addition of animals among repeated ones
        cage_1.add_animals(list_1)
        self.assertEqual(cage_1.animals_list, list_1)              
            # Tests zoo with populated cages
        zoo.add_cages(list_3)
        self.assertEqual(zoo.cages, list_3)
        
    def initiate_competition(self):
            # Tests attempt to add animals in different orders of competition
        cage_2.add_animals(list_2)
        self.assertEqual(cage_2.animals_list, list_2)

        
        # Tests competition between prey and predator
        
        
        # Tests if animal already in another cage 
        #### Should I do it?
        
        
#         self.assertTrue()
        
""" 
Only if file is primarily called on Python (executed by its name) 
the main() function will be called and tests will be initiated. 
"""          
if __name__ == '__main__':
    main()
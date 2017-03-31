from zoo import (Zoo, Cage, Animal, Mouse, Goat, Rabbit, Jackal, Owl, Snake,
                 Kite, WildCat, Lion)
from unittest import TestCase, main

class ZooScenario(TestCase):
    
    def setUp(self):
        zoo = Zoo()
        cage = Cage()
        animal = Animal()
        
    
    def test_requirements(self):
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

        list_1 = [mouse_2, snake_1, goat_1, mouse_2, goat_1, mouse_2, owl_1,
                  rabbit_2]
        list_2 = [lion_2, mouse_3, snake_1, jackal_1, rabbit_1, mouse_1]
        list_of_cages = [cage_1, cage_2, cage_3]
        

        # Tests zoo with empty cages
        zoo.add_cages(list_of_cages)
        self.assertEqual(zoo.cages, list_of_cages)
        # Tests multiple addition of animals among repeated ones
        cage_1.animals_list = []
        cage_1.add_animals(list_1)
        self.assertEqual(cage_1.animals_list, list_1)              
        # Tests zoo with populated cages
        zoo.cages = []
        zoo.add_cages(list_of_cages)
        self.assertEqual(zoo.cages, list_of_cages)
        
        
        # Tests attempt to add animals in different orders of competition
        cage_2.animals_list = []
        cage_2.add_animals(list_2)
        self.assertEqual(cage_2.animals_list, list_2)


        
        # Tests competition between prey and predator
        
        
        # Tests if animal already in another cage 
        #### Should I do it?
        
        
        
        # Attempt to add objects that are not animals to a cage
        cage_3.animals_list = []
        cage_3.add_animals([2])
        self.assertFalse(cage_3.animals_list, [2])
        cage_3.animals_list = []
        cage_3.add_animals([zoo])
        self.assertFalse(cage_3.animals_list, [zoo])
        
        # Attempt to add objects that are not cages to a zoo
        zoo.add_cages(['Cage 1'])
        self.assertFalse(zoo.cages, ['Cage 1'])
        zoo.add_cages([owl_1])
        self.assertFalse(zoo.cages, [owl_1])
        
        
        
        
        
        
#         self.assertTrue()

""" Only if file is primarily called on Python (executed by its name)
the main() function will be called and tests will be initiated.
"""
if __name__ == '__main__':
    main()

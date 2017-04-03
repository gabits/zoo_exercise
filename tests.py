from zoo import (Zoo, Cage, Animal, Mouse, WildCat, Lion)
from unittest import TestCase, main

class UserStory(TestCase):

    def test_requirements(self):
        """ Creates zoo and cages: """
        zoo = Zoo()
        cage_1 = Cage()
        cage_2 = Cage()

        """ Creation of animals: """
        mouse = Mouse()
        wildcat = WildCat()
        lion = Lion()      

        """ Attempt to add objects that are not cages to a zoo """
        zoo.add_cages(['Cage 1'])
        self.assertFalse(zoo.cages, ['Cage 1'])
        zoo.add_cages([mouse])
        self.assertFalse(zoo.cages, [mouse])

        """ Tests zoo with empty cages """
        zoo.add_cages([cage_1, cage_2])
        self.assertEqual(zoo.cages, [cage_1, cage_2])

        """ Multiple addition of animals among repeated ones """
        cage_1.add_animals([mouse, mouse, lion, lion, mouse])
        # Set up to test more than one duplicated animal and different orders
        self.assertEqual(cage_1.animals_list, [mouse, lion])

        """ Tests zoo with populated cages """
        zoo.cages = []
        zoo.add_cages([cage_1, cage_2])
        self.assertEqual(zoo.cages, [cage_1, cage_2])

        """ Tests competition between prey and predator """
        cage_2.add_animals([mouse, wildcat, lion])
        self.assertEqual(cage_2.animals_list, [lion])

        """ Tests if animal already in another cage """
        # ----- Should I do it?

        """ Attempt to add objects that are not animals to a cage """
        cage_1.animals_list = []
        cage_1.add_animals([2])
        self.assertFalse(cage_1.animals_list, [2])
        cage_1.add_animals([zoo])
        self.assertFalse(cage_1.animals_list, [zoo])

#         self.assertTrue()

""" Only if file is primarily called on Python (executed by its name)
the main() function will be called and tests will be initiated.
"""
if __name__ == '__main__':
    main()

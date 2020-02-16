import unittest

from jour6.jour6 import treatment, make_tree


class MyTestCase(unittest.TestCase):

    def test_treatment_part_1(self):
        my_list = ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L"]
        root_name = "COM"
        tree = make_tree(my_list, root_name)
        self.assertEqual(treatment(my_list, tree), 42, True)


if __name__ == '__main__':
    unittest.main()

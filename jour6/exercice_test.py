import unittest

from jour6.exercice import treatement


class MyTestCase(unittest.TestCase):

    def test_treatment_part_1(self):
        my_list = ["COM)B\n", "B)C\n", "C)D\n", "D)E\n", "E)F\n", "B)G\n", "G)H\n", "D)I\n", "E)J\n", "J)K\n", "K)L\n"]
        self.assertEqual(treatement(my_list, "COM"), 42, "KO")


if __name__ == '__main__':
    unittest.main()

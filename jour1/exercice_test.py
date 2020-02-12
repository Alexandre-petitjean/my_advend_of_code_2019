import unittest

from jour1.exercice import calculate_part_1, calculate_part_2


class MyTestCase(unittest.TestCase):

    def test_calculation_part1_12(self):
        my_list = [12]
        self.assertEqual(calculate_part_1(my_list), 2, "KO")

    def test_calculation_part1_14(self):
        my_list = [14]
        self.assertEqual(calculate_part_1(my_list), 2, "KO")

    def test_calculation_part1_1969(self):
        my_list = [1969]
        self.assertEqual(calculate_part_1(my_list), 654, "KO")

    def test_calculation_part1_100756(self):
        my_list = [100756]
        self.assertEqual(calculate_part_1(my_list), 33583, "KO")

    def test_calculation_part2_14(self):
        my_list = [14]
        self.assertEqual(calculate_part_2(my_list), 2, "KO")

    def test_calculation_part2_1969(self):
        my_list = [1969]
        self.assertEqual(calculate_part_2(my_list), 966, "KO")

    def test_calculation_part2_100756(self):
        my_list = [100756]
        self.assertEqual(calculate_part_2(my_list), 50346, "KO")


if __name__ == '__main__':
    unittest.main()

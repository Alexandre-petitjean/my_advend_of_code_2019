"""
Test of the day 1 of the Advent of code
--- The Tyranny of the Rocket Equation ---
"""
import unittest

from day1.day_1 import calculate_part_1, calculate_part_2


class MyTestCase(unittest.TestCase):

    def test_calculation_part1(self):
        my_list = [12]
        self.assertEqual(calculate_part_1(my_list), 2, "KO")

        my_list = [14]
        self.assertEqual(calculate_part_1(my_list), 2, "KO")

        my_list = [1969]
        self.assertEqual(calculate_part_1(my_list), 654, "KO")

        my_list = [100756]
        self.assertEqual(calculate_part_1(my_list), 33583, "KO")

    def test_calculation_part2(self):
        my_list = [14]
        self.assertEqual(calculate_part_2(my_list), 2, "KO")

        my_list = [1969]
        self.assertEqual(calculate_part_2(my_list), 966, "KO")

        my_list = [100756]
        self.assertEqual(calculate_part_2(my_list), 50346, "KO")


if __name__ == '__main__':
    unittest.main()

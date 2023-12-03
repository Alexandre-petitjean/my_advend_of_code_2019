

import unittest

from year_2021.day2.main import calc_location_part1, calc_location_part2


class MyTestCase(unittest.TestCase):

    def test_calc_part1(self):
        my_list = ['forward 5', 'down 5','forward 8', 'up 3', 'down 8', 'forward 2']
        self.assertEqual(calc_location_part1(my_list), 150, "KO")

    def test_calc_part2(self):
        my_list = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']
        self.assertEqual(calc_location_part2(my_list), 900, "KO")
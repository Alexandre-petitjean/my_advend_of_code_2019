import unittest

from year_2021.day1.main import calc_nb_augmentation, calc_nb_augmentation_by_groupe


class MyTestCase(unittest.TestCase):

    def test_calc_part1(self):
        my_list = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        self.assertEqual(calc_nb_augmentation(my_list), 7, "KO")

    def test_calc_part2(self):
        my_list = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        self.assertEqual(calc_nb_augmentation_by_groupe(my_list), 5, "KO")
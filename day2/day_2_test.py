"""
Test for the Day 2.
"""
import unittest

from day2.day_2 import treatment


class MyTestCase(unittest.TestCase):

    def test_treatment(self):
        my_list = [1, 0, 0, 0, 99]
        self.assertEqual(treatment(my_list), 2, "KO")

        my_list = [2, 3, 0, 3, 99]
        self.assertEqual(treatment(my_list), 2, "KO")

        my_list = [2, 4, 4, 5, 99, 0]
        self.assertEqual(treatment(my_list), 2, "KO")

        my_list = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        self.assertEqual(treatment(my_list), 30, "KO")

        my_list = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        self.assertEqual(treatment(my_list), 3500, "KO")


if __name__ == '__main__':
    unittest.main()

import unittest

from day2.day_2 import treatment_part_1


class MyTestCase(unittest.TestCase):

    def test_treatment_part_1_1(self):
        my_list = [1, 0, 0, 0, 99]
        self.assertEqual(treatment_part_1(my_list), 2, "KO")

    def test_treatment_part_1_2(self):
        my_list = [2, 3, 0, 3, 99]
        self.assertEqual(treatment_part_1(my_list), 2, "KO")

    def test_treatment_part_1_3(self):
        my_list = [2, 4, 4, 5, 99, 0]
        self.assertEqual(treatment_part_1(my_list), 2, "KO")

    def test_treatment_part_1_4(self):
        my_list = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        self.assertEqual(treatment_part_1(my_list), 30, "KO")

    def test_treatment_part_1_5(self):
        my_list = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        self.assertEqual(treatment_part_1(my_list), 3500, "KO")


if __name__ == '__main__':
    unittest.main()

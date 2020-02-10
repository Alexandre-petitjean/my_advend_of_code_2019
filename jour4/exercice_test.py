import unittest

from jour4.exercice import digit_never_decrease, same_adj_digit


class MyTestCase(unittest.TestCase):

    borne_min = 273025
    borne_max = 767253

    def test_decreasing_number(self):
        my_number = 223450
        self.assertEqual(digit_never_decrease(my_number), False)

    def test_no_double_number(self):
        my_number = 123789
        self.assertEqual(same_adj_digit(my_number), False)

    def test_double_number(self):
        my_number = 112233
        self.assertEqual(same_adj_digit(my_number), True)
        self.assertEqual(digit_never_decrease(my_number), True)

    def test_double_number_part_2(self):
        my_number = 123444
        self.assertEqual(same_adj_digit(my_number), False, "123444 is not good")

    def test_double_number_good_part_2(self):
        my_number = 112222
        self.assertEqual(same_adj_digit(my_number), True)

    def test_double_number_good_part_2_2(self):
        my_number = 111122
        self.assertEqual(same_adj_digit(my_number), True)

    def test_double_number_good_part_2_3(self):
        my_number = 133456
        self.assertEqual(same_adj_digit(my_number), False)

    # def test_good_number_part_1(self):
    #     my_number = 111111
    #     self.assertEqual(same_adj_digit(my_number), True)
    #     self.assertEqual(digit_never_decrease(my_number), True)


if __name__ == '__main__':
    unittest.main()

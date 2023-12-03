import unittest

from day4.day_4 import digit_never_decrease, same_adj_digit_part1, same_adj_digit_part2


class MyTestCase(unittest.TestCase):
    borne_min = 273025
    borne_max = 767253

    def test_number(self):
        my_number = 223450
        self.assertEqual(digit_never_decrease(my_number), False)

        my_number = 123789
        self.assertEqual(same_adj_digit_part1(my_number), False)

        my_number = 112233
        self.assertEqual(same_adj_digit_part1(my_number), True)
        self.assertEqual(digit_never_decrease(my_number), True)

    def test_part_2(self):
        my_number = 123444
        self.assertEqual(same_adj_digit_part2(my_number), False, "123444 is not good")

        my_number = 112222
        self.assertEqual(same_adj_digit_part2(my_number), True)

        my_number = 111122
        self.assertEqual(same_adj_digit_part2(my_number), True)

        my_number = 133456
        self.assertEqual(same_adj_digit_part2(my_number), True)


if __name__ == '__main__':
    unittest.main()

import unittest

from year_2020.day1.day1 import find_sum_2020_part1, find_sum_2020_part2


class MyTestCase(unittest.TestCase):

    input = [1721, 979, 366, 299, 675, 1456]

    def test_part1(self):
        self.assertEqual(find_sum_2020_part1(input), 514579)

    def test_part2(self):
        self.assertEqual(find_sum_2020_part2(input), 241861950)


if __name__ == '__main__':
    unittest.main()

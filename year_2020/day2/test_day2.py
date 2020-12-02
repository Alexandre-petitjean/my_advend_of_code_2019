import unittest


class MyTestCase(unittest.TestCase):


    def test_part1(self):
        self.assertEqual(find_sum_2020_part1(input), 514579)

    def test_part2(self):
        pass


if __name__ == '__main__':
    unittest.main()
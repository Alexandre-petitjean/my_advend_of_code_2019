import unittest

from year_2020.day2.day2 import nb_of_valid_pwd


class MyTestCase(unittest.TestCase):

    LIST = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]

    def test_part1(self):
        self.assertEqual(nb_of_valid_pwd(self.LIST, 1), 2)

    def test_part2(self):
        self.assertEqual(nb_of_valid_pwd(self.LIST, 2), 1)


if __name__ == '__main__':
    unittest.main()

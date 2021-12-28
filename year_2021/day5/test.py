import unittest

from year_2021.day5.main import dessine_carte, count_number


class MyTestCase(unittest.TestCase):
    lignes = [
        [2, 2, 2, 1],
        [0, 9, 5, 9],
        [0, 9, 2, 9],
        [1, 4, 9, 4],
        [7, 0, 7, 4],
        [3, 4, 3, 4]
    ]

    def test_partie(self):
        carte = dessine_carte(self.lignes)
        self.assertEqual(5, count_number(carte, 2))


if __name__ == '__main__':
    unittest.main()

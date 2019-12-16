import unittest

from exo1.exercice import calcule


class MyTestCase(unittest.TestCase):

    def test_calcule_12(self):
        my_list = [12]
        self.assertEqual(calcule(my_list), 2, "KO")

    def test_calcule_14(self):
        my_list = [14]
        self.assertEqual(calcule(my_list), 2, "KO")

    def test_calcule_1969(self):
        my_list = [1969]
        self.assertEqual(calcule(my_list), 654, "KO")

    def test_calcule_100756(self):
        my_list = [100756]
        self.assertEqual(calcule(my_list), 33583, "KO")


if __name__ == '__main__':
    unittest.main()

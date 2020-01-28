import unittest

from jour2.exercice import treatment_part_1


class MyTestCase(unittest.TestCase):

    def test_treatment_part_2(self):
        my_list = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
        self.assertEqual(treatment_part_1(my_list), 2, "KO")


if __name__ == '__main__':
    unittest.main()

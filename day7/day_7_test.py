import unittest

from day7.day_7 import treatment


class MyTestCase(unittest.TestCase):

    def test_treatment_part_1_1(self):
        software = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]
        amplifier_input = [[4, 3, 2, 1, 0]]
        self.assertEqual(treatment(software, amplifier_input), 43210, True)

    def test_treatment_part_1_2(self):
        software = [3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23,
                    101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0]
        amplifier_input = [[0, 1, 2, 3, 4]]
        self.assertEqual(treatment(software, amplifier_input), 54321, True)

    def test_treatment_part_1_3(self):
        software = [3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33,
                    1002, 33, 7, 33, 1, 33, 31, 31, 1, 32, 31, 31, 4, 31, 99, 0, 0, 0]
        amplifier_input = [[1, 0, 4, 3, 2]]
        self.assertEqual(treatment(software, amplifier_input), 65210, True)

    def test_treatment_part_2_1(self):
        software = [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26,
                    27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5]
        amplifier_input = [[9, 8, 7, 6, 5]]
        self.assertEqual(treatment(software, amplifier_input), 139629729, True)


if __name__ == '__main__':
    unittest.main()

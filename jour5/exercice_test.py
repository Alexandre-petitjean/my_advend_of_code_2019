import unittest

from jour5.exercice import treatment


class MyTestCase(unittest.TestCase):
    # TEST OPCODE 5 & 6
    def test_opcode5_immmode_0(self):
        my_list = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
        self.assertEqual(treatment(my_list, 0), 0, "KO")

    def test_opcode5_immmode_1(self):
        my_list = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
        self.assertEqual(treatment(my_list, 1), 1, "KO")

    def test_opcode6_posmode_0(self):
        my_list = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
        self.assertEqual(treatment(my_list, 0), 0, "KO")

    def test_opcode6_posmode_1(self):
        my_list = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
        self.assertEqual(treatment(my_list, 1), 1, "KO")

    # TEST OPCODE 7
    def test_opcode7_posmode_0(self):
        my_list = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
        self.assertEqual(treatment(my_list, 8), 0, "KO")

    def test_opcode7_posmode_1(self):
        my_list = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
        self.assertEqual(treatment(my_list, 7), 1, "KO")

    def test_opcode7_immmode_0(self):
        my_list = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
        self.assertEqual(treatment(my_list, 8), 0, "KO")

    def test_opcode7_immmode_1(self):
        my_list = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
        self.assertEqual(treatment(my_list, 7), 1, "KO")

    # TEST OPCODE 8
    def test_opcode8_posmode_0(self):
        my_list = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
        self.assertEqual(treatment(my_list, 8), 1, "KO")

    def test_opcode8_posmode_1(self):
        my_list = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
        self.assertEqual(treatment(my_list, 1), 0, "KO")

    def test_opcode8_immmode_0(self):
        my_list = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
        self.assertEqual(treatment(my_list, 8), 1, "KO")

    def test_opcode8_immmode_1(self):
        my_list = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
        self.assertEqual(treatment(my_list, 1), 0, "KO")

    def test_all_999(self):
        my_list = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                   1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                   999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
        self.assertEqual(treatment(my_list, 6), 999, "KO")

    def test_all_1000(self):
        my_list = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                   1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                   999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
        self.assertEqual(treatment(my_list, 8), 1000, "KO")

    def test_all_1001(self):
        my_list = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                   1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                   999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
        self.assertEqual(treatment(my_list, 9), 1001, "KO")


if __name__ == '__main__':
    unittest.main()

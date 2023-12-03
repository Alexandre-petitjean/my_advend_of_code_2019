"""
Test of day 3
"""

import unittest

from day3.day_3 import treatment_part1, treatment_part2


class MyTestCase(unittest.TestCase):

    def test_part1_1(self):

        my_list = [["R8", "U5", "L5", "D3"], ["U7", "R6", "D4", "L4"]]
        self.assertEqual(treatment_part1(my_list), 6, True)

        my_list = [["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"],
                   ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"]]
        self.assertEqual(treatment_part1(my_list), 159, True)

        my_list = [["R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33", "U53", "R51"],
                   ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"]]
        self.assertEqual(treatment_part1(my_list), 135, True)

    def test_part2(self):

        my_list = [["R8", "U5", "L5", "D3"], ["U7", "R6", "D4", "L4"]]
        self.assertEqual(treatment_part2(my_list), 30, True)

        my_list = [["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"],
                   ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"]]
        self.assertEqual(treatment_part2(my_list), 610, True)

        my_list = [["R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33", "U53", "R51"],
                   ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"]]
        self.assertEqual(treatment_part2(my_list), 410, True)


if __name__ == '__main__':
    unittest.main()

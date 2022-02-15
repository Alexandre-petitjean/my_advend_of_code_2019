import unittest

from year_2021.day7.main import findBestPosPart1, findBestPosPart2


class MyTestCase(unittest.TestCase):
    input_list = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

    def testSamePosPart1(self):
        self.assertEqual(37, findBestPosPart1(self.input_list))

    def testSamePosePart2(self):
        self.assertEqual(168, findBestPosPart2(self.input_list))

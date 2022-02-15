import unittest

from year_2021.day7.main import findBestPos


class MyTestCase(unittest.TestCase):
    input_list = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

    def testSamePos(self):
        self.assertEqual(37, findBestPos(self.input_list))

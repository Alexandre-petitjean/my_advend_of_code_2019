import unittest

from day8.day_8 import explode_size, treatment_part_2


class MyTestCase(unittest.TestCase):

    def test_part2(self):
        my_list = ["0222112222120000"]

        wide = 2
        tall = 2
        size = wide * tall
        my_list = explode_size(my_list, size)
        self.assertEqual(treatment_part_2(my_list))


if __name__ == '__main__':
    unittest.main()

import unittest

from year_2021.day6.main import get_lantern_fish_list, status_lantern_fish, spawn_lanternfish


class MyTestCase(unittest.TestCase):
    lignes = [3, 4, 3, 1, 2]

    def test_partie(self):
        lantern_fish_list = get_lantern_fish_list(self.lignes)
        self.assertEqual(spawn_lanternfish(lantern_fish_list, 18), 26)
        lantern_fish_list = get_lantern_fish_list(self.lignes)
        self.assertEqual(spawn_lanternfish(lantern_fish_list, 80), 5934)


if __name__ == '__main__':
    unittest.main()

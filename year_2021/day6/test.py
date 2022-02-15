import unittest

from year_2021.day6.main import spawn_lanternfish, get_lantern_fish_dict


class MyTestCase(unittest.TestCase):

    lignes = [3, 4, 3, 1, 2]

    def setUp(self) -> None:
        self.lantern_fish_dict = get_lantern_fish_dict(self.lignes)

    def test_18(self):
        self.assertEqual(spawn_lanternfish(self.lantern_fish_dict, 18), 26)

    def test_80(self):
        self.assertEqual(spawn_lanternfish(self.lantern_fish_dict, 80), 5934)

    def test_256(self):
        self.assertEqual(spawn_lanternfish(self.lantern_fish_dict, 256), 26984457539)


if __name__ == '__main__':
    unittest.main()

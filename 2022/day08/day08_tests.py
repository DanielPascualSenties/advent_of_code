import unittest

from day08 import element, is_it_visible, day_08, get_input, is_it_visible_south, is_it_visible_north, \
    is_it_visible_east, is_it_visible_west, \
    day_08_part2, count_trees_north, count_trees_south, count_trees_east, count_trees_west


class TestDay08(unittest.TestCase):
    def test_is_it_visible_north(self):
        self.assertEqual(True, is_it_visible_north(5, 1, 1, get_input("day08_example.txt")))
        self.assertEqual(False, is_it_visible_north(5, 2, 1, get_input("day08_example.txt")))

    def test_is_it_visible_south(self):
        self.assertEqual(True, is_it_visible_south(5, 3, 2, get_input("day08_example.txt")))
        self.assertEqual(False, is_it_visible_south(4, 3, 3, get_input("day08_example.txt")))

    def test_is_it_visible_east(self):
        self.assertEqual(True, is_it_visible_east(5, 1, 2, get_input("day08_example.txt")))
        self.assertEqual(False, is_it_visible_east(1, 1, 3, get_input("day08_example.txt")))

    def test_is_it_visible_west(self):
        self.assertEqual(True, is_it_visible_west(5, 3, 2, get_input("day08_example.txt")))
        self.assertEqual(False, is_it_visible_west(5, 2, 1, get_input("day08_example.txt")))

    def test_count_trees_north(self):
        self.assertEqual(1, count_trees_north(5, 1, 2, get_input("day08_example.txt")))
        self.assertEqual(2, count_trees_north(5, 3, 2, get_input("day08_example.txt")))

    def test_count_trees_south(self):
        self.assertEqual(2, count_trees_south(5, 1, 2, get_input("day08_example.txt")))
        self.assertEqual(1, count_trees_south(5, 3, 2, get_input("day08_example.txt")))

    def test_count_trees_east(self):
        self.assertEqual(2, count_trees_east(5, 1, 2, get_input("day08_example.txt")))
        self.assertEqual(2, count_trees_east(5, 3, 2, get_input("day08_example.txt")))

    def test_count_trees_west(self):
        self.assertEqual(1, count_trees_west(5, 1, 2, get_input("day08_example.txt")))
        self.assertEqual(2, count_trees_west(5, 3, 2, get_input("day08_example.txt")))

    def test_element(self):
        self.assertEqual(3, element(location_row=0, location_col=0, dataframe=get_input("day08_example.txt")))
        self.assertEqual(0, element(location_row=0, location_col=1, dataframe=get_input("day08_example.txt")))
        self.assertEqual(2, element(location_row=1, location_col=0, dataframe=get_input("day08_example.txt")))

    def test_day_08(self):
        self.assertEqual(21, day_08("day08_example.txt"))

    def test_day_08_part2(self):
        self.assertEqual(8, day_08_part2("day08_example.txt"))

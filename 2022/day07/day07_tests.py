import unittest
from day07 import day_07, count_condition


class TestDay07(unittest.TestCase):
    def test_count_condition(self):
        self.assertEqual(95437, count_condition({'/': 48381165, 'a': 94853, 'd': 24933642, 'e': 584}))

    def test_day_07(self):
        self.assertEqual(95437, day_07("day07_example.txt"))

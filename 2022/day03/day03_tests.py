import unittest
from day03 import day03, split_string_half, find_coincidences, numeric_value, day03_part2


class TestDay03(unittest.TestCase):
    def test_part2(self):
        self.assertEqual(70, day03_part2("day03_example.txt"))

    def test_split_string_half(self):
        self.assertEqual(["abc", "def"], split_string_half("abcdef"))

    def test_find_coincidences(self):
        self.assertEqual({"a"}, find_coincidences("abc", "efa"))

    def test_part1(self):
        self.assertEqual(157, day03("day03_example.txt"))

    def test_numeric_value(self):
        self.assertEqual(16, numeric_value("p"))
        self.assertEqual(38, numeric_value("L"))
        self.assertEqual(42, numeric_value("P"))
        self.assertEqual(22, numeric_value("v"))
        self.assertEqual(20, numeric_value("t"))
        self.assertEqual(19, numeric_value("s"))

import unittest
from day04 import split_into_tuples, check_overlapping, day04, check_strict_overlapping, day04_part2


class TestDay04(unittest.TestCase):
    def test_part01(self):
        self.assertEqual(2, day04("day04_example.txt"))

    def test_part02(self):
        self.assertEqual(4, day04_part2("day04_example.txt"))

    def test_split_into_tuples(self):
        self.assertEqual((('2', '4'), ('6', '8')), split_into_tuples("2-4,6-8"))

    def test_check_overlapping(self):
        self.assertEqual(True, check_overlapping((1, 5), (2, 4)))
        self.assertEqual(True, check_overlapping((2, 4), (1, 5)))
        self.assertEqual(True, check_overlapping((1, 5), (1, 5)))
        self.assertEqual(False, check_overlapping((1, 5), (6, 10)))
        self.assertEqual(False, check_overlapping((1, 6), (5, 10)))

    def test_check_strict_overlapping(self):
        self.assertEqual(True, check_strict_overlapping((1, 5), (2, 4)))
        self.assertEqual(True, check_strict_overlapping((2, 4), (1, 5)))
        self.assertEqual(True, check_strict_overlapping((1, 5), (1, 5)))
        self.assertEqual(False, check_strict_overlapping((1, 5), (6, 10)))
        self.assertEqual(True, check_strict_overlapping((1, 6), (5, 10)))

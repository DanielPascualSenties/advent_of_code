import unittest
from day06 import ingest_message, has_duplicates, day_06


class TestDay06(unittest.TestCase):

    def test_ingest_message(self):
        self.assertEqual("bvwbjplbgvbhsrlpgdmjqwftvncz", ingest_message("day06_examples.txt", 0))
        self.assertEqual("nppdvjthqldpwncqszvftbrmjlhg", ingest_message("day06_examples.txt", 1))
        self.assertEqual("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", ingest_message("day06_examples.txt", 2))
        self.assertEqual("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", ingest_message("day06_examples.txt", 3))

    def test_has_duplicates(self):
        self.assertEqual(False, has_duplicates("abcd"))
        self.assertEqual(True, has_duplicates("abca"))

    def test_day06(self):
        self.assertEqual(5, day_06("day06_examples.txt", 0, 4))
        self.assertEqual(6, day_06("day06_examples.txt", 1, 4))
        self.assertEqual(10, day_06("day06_examples.txt", 2, 4))
        self.assertEqual(11, day_06("day06_examples.txt", 3, 4))

    def test_day06_part2(self):
        self.assertEqual(19, day_06("day06_examples.txt", 4, 14))
        self.assertEqual(23, day_06("day06_examples.txt", 5, 14))
        self.assertEqual(23, day_06("day06_examples.txt", 6, 14))
        self.assertEqual(29, day_06("day06_examples.txt", 7, 14))
        self.assertEqual(26, day_06("day06_examples.txt", 8, 14))

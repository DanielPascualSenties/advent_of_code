import unittest
from day05 import ingest_crates, ingest_move, make_move, read_top, day_05, make_move_part2, day_05_part2


class TestDay05(unittest.TestCase):

    def test_day_05(self):
        self.assertEqual("CMZ", day_05(input_name="day05_example.txt"))

    def test_day_05_part2(self):
        self.assertEqual("MCD", day_05_part2(input_name="day05_example.txt"))

    def test_ingest_crates(self):
        self.assertEqual({1: ["Z"], 2: ["M"], 3: ["P"]}, ingest_crates("[Z] [M] [P]", {1: [], 2: [], 3: []}))

    def test_read_crates(self):
        self.assertEqual({1: ['N', 'Z'], 2: ['D', 'C', 'M'], 3: ['P']}, {1: ['N', 'Z'], 2: ['D', 'C', 'M'], 3: ['P']})

    def test_read_top(self):
        self.assertEqual("CMZ", read_top({1: ["C"], 2: ["M"], 3: ["Z"]}))
        self.assertEqual("CMZ", read_top({1: ["C"], 2: ["M"], 3: ["Z", "N", "D", "P"]}))

    def test_ingest_move(self):
        self.assertEqual((1, 2, 1), ingest_move("move 1 from 2 to 1"))
        self.assertEqual((3, 1, 3), ingest_move("move 3 from 1 to 3"))
        self.assertEqual((2, 2, 1), ingest_move("move 2 from 2 to 1"))
        self.assertEqual((1, 1, 2), ingest_move("move 1 from 1 to 2"))

    def test_make_move(self):
        self.assertEqual({1: ['A', 'A'], 2: [], 3: ['A']}, make_move((1, 2, 1), {1: ['A'], 2: ['A'], 3: ['A']}))
        self.assertEqual({1: ['B', 'A'], 2: ["C"], 3: ['D']}, make_move((1, 2, 1), {1: ['A'], 2: ['B', "C"], 3: ['D']}))
        self.assertEqual({1: ['B', 'A'], 2: [], 3: ['C']}, make_move((1, 2, 1), {1: ['A'], 2: ['B'], 3: ['C']}))

    def test_make_move_part2(self):
        self.assertEqual({1: ['A', 'A'], 2: [], 3: ['A']}, make_move((1, 2, 1), {1: ['A'], 2: ['A'], 3: ['A']}))
        self.assertEqual({1: ['B', 'A'], 2: ["C"], 3: ['D']}, make_move((1, 2, 1), {1: ['A'], 2: ['B', "C"], 3: ['D']}))
        self.assertEqual({1: ['B', 'A'], 2: [], 3: ['C']}, make_move((1, 2, 1), {1: ['A'], 2: ['B'], 3: ['C']}))


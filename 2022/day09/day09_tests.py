import unittest
from day09 import move, day09, pull, day09_part2


class MyTestCase(unittest.TestCase):

    def test_move(self):
        self.assertEqual((1, 0), move((0, 0), (0, 0), 'U')[0])
        self.assertEqual((0, 1), move((0, 0), (0, 0), 'R')[0])
        self.assertEqual((0, 0), move((1, 0), (0, 0), 'D')[0])
        self.assertEqual((0, 0), move((0, 1), (0, 0), 'L')[0])

    def test_day09(self):
        self.assertEqual(13, day09("day09_example.txt"))

    def test_pull(self):
        self.assertEqual((0, 1), pull((0, 2), (0, 0)))
        self.assertEqual((1, 1), pull((1, 2), (0, 0)))
        self.assertEqual((-1, 1), pull((-1, 2), (0, 0)))
        self.assertEqual((1, 1), pull((0, 0), (2, 2)))


    def test_day09_part2(self):
        self.assertEqual(1, day09_part2("day09_example.txt"))
        self.assertEqual(36, day09_part2("day09_part2_example.txt"))


if __name__ == '__main__':
    unittest.main()

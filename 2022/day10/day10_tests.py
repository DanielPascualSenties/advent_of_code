import unittest
from day10 import is_relevant, generate_stack, day10


class MyTestCase(unittest.TestCase):
    def test_is_relevant(self):
        self.assertEqual(True, is_relevant(20))
        self.assertEqual(False, is_relevant(40))
        self.assertEqual(True, is_relevant(60))
        self.assertEqual(False, is_relevant(80))
        self.assertEqual(False, is_relevant(21))

    def test_generate_stack(self):
        self.assertEqual(['noop', 'Operating', '3', 'Operating', '-5'], generate_stack("day10_toy_example.txt"))


    def test_day10(self):
        self.assertEqual(0, day10("day10_toy_example.txt"))
        self.assertEqual(13140, day10("day10_example.txt"))


if __name__ == '__main__':
    unittest.main()

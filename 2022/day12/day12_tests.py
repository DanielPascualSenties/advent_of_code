import unittest
from day12 import day12


class MyTestCase(unittest.TestCase):
    def test_day12(self):
        self.assertEqual(31, day12("day12_example.txt"))  # add assertion here




if __name__ == '__main__':
    unittest.main()

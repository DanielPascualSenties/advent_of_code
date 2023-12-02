import unittest
from day01 import get_calibration_value, day_01


class MyTestCase(unittest.TestCase):
    def test_calibration_value(self):
        self.assertEqual(get_calibration_value("1abc2"), 12)
        self.assertEqual(get_calibration_value("pqr3stu8vwx"), 38)
        self.assertEqual(get_calibration_value("a1b2c3d4e5f"), 15)
        self.assertEqual(get_calibration_value("treb7uchet"), 77)

    def test_day01(self):
        self.assertEqual(day_01("day01_example.txt"), 142)


if __name__ == '__main__':
    unittest.main()

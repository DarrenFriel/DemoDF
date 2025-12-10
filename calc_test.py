"""Unit tests for the BasicCalc class from basic_calc module."""

import unittest
from basic_calc import BasicCalc

class TestCalc(unittest.TestCase):
    """Unit tests for BasicCalc class."""

    def setUp(self):
        """Create a calculator instance before each test."""
        self.calc = BasicCalc()

    def test_add(self):
        """Test addition method."""
        self.assertEqual(5, self.calc.add(2, 3))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(-5, self.calc.add(-2, -3))

    def test_sub(self):
        """Test subtraction method."""
        self.assertEqual(1, self.calc.sub(3, 2))
        self.assertEqual(-3, self.calc.sub(-1, 2))
        self.assertEqual(1, self.calc.sub(-2, -3))

if __name__ == '__main__':
    unittest.main()

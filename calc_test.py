#tests for calculator class
import unittest
from basic_calc import BasicCalc

class TestCalc(unittest.TestCase):

    def test_add(self):
        calc = BasicCalc()
        self.assertEqual(5, calc.add(2, 3))
        self.assertEqual(0, calc.add(-2, 2))
        self.assertEqual(-5, calc.add(-2, -3))
    def test_sub(self):
        calc = BasicCalc()
        self.assertEqual(1, calc.sub(3, 2))
        self.assertEqual(-3, calc.sub(-1, 2))
        self.assertEqual(1, calc.sub(-2, -3))
if __name__ == '__main__':
    unittest.main()

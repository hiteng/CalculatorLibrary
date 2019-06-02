
"""
Unit tests for the calculator library
"""
import unittest
from calculator import add, subtract, mul


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(subtract(4, 2), 2)

    def test_mul(self):
        self.assertEqual(mul(1, 3), 3)

    # def test_addition(self):
    #     assert 4 == calculator.add(2, 2)
    #
    # def test_subtraction(self):
    #     assert 2 == calculator.subtract(4, 2)

if __name__ == '__main__':
    unittest.main()
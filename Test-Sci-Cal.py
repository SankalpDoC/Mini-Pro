import unittest
from SciCal import *

class TestCalculator(unittest.TestCase):

    def test_square_root(self):
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(16), 4)
        
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        
    def test_natural_logarithm(self):
        self.assertAlmostEqual(natural_logarithm(1), 0)
        self.assertAlmostEqual(natural_logarithm(math.e), 1)
        
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(10, 0), 1)
        self.assertAlmostEqual(power(2, 0.5), math.sqrt(2))
        

if __name__ == '__main__':
    unittest.main()

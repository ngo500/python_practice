"""
Unit testing for mod module's functions square and double
"""
import unittest
from mod import square, double

"""
Class that contains unit tests for square function
"""
class TestSquare(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(2), 4)
        self.assertEqual(square(3.0), 9.0)
        self.assertNotEqual(square(-3), -9) #must NOT equal

"""
Class that contains unit tests for double function
"""
class TestDouble(unittest.TestCase):
    def test_double(self):
        self.assertEqual(double(2), 4)
        self.assertEqual(double(-3.1), -6.2)
        self.assertEqual(double(0), 0)

unittest.main() #run the tests

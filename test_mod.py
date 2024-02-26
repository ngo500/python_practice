"""
Unit testing for mod module's functions square, double, and add
"""
import unittest
from mod import square, double, add

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

"""
Class that contains unit tests for add function
"""
class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 4), 6)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(2.3, 3.6), 5.9)
        self.assertEqual(add('hello', 'world'), 'helloworld')
        self.assertEqual(add(2.3000, 4.300), 6.6)
        self.assertNotEqual(add(-2, -2), 0)

unittest.main() #run the tests

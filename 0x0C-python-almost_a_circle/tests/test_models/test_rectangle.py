#!/usr/bin/python3
"""Unittest for the base.py rectangle module
"""

import unittest
import sys
import io
from models.rectangle import Rectangle
from contextlib import redirect_stdout


class RectidTest(unittest.TestCase):
    r1 = Rectangle(10, 2)
    r2 = Rectangle(2, 10)
    r3 = Rectangle(10, 2, 1, 0, 12)

    def test_objectsid(self):
        """test id allocation"""
        self.assertEqual(RectidTest.r3.id, 12)

    def test_get(self):
        """test getters"""
        self.assertEqual(RectidTest.r1.width, 10)
        self.assertEqual(RectidTest.r3.x, 1)

    def test_set(self):
        RectidTest.r1.y = 10
        RectidTest.r2.x = 30
        self.assertEqual(RectidTest.r1.y, 10)
        self.assertEqual(RectidTest.r2.x, 30)


class validator(unittest.TestCase):
    """A test case"""
    r4 = Rectangle(10, 2)
    r5 = Rectangle(2, 10)
    r6 = Rectangle(10, 2, 1, 0, 12)

    def test_area(self):
        """test area property"""
        x = validator.r6.area()
        self.assertEqual(x, 20.0)

    def test_heightwidth(self):
        """test height and width validator"""
        validator.r6.height = 10
        self.assertEqual(validator.r6.height, 10)
        with self.assertRaises(ValueError):
            validator.r6.height = 0

    def test_xy(self):
        """test x and y validator"""
        validator.r4.x = 10
        self.assertEqual(validator.r4.x, 10)
        with self.assertRaises(TypeError):
            validator.r4.x = 1.0

    def test_type(self):
        """test type error"""
        validator.r5.width = 10
        self.assertEqual(validator.r5.width, 10)
        with self.assertRaises(TypeError):
            validator.r5.width = "-10"

    def test_display(self):
        """checks if display function completed successfully"""
        suppress_text = io.StringIO()
        sys.stdout = suppress_text
        self.assertTrue(validator.r5.display())
        sys.stdout = sys.__stdout__

    def test_6(self):
        """tests method __str__"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        output = ""
        with io.StringIO() as buf, redirect_stdout(buf):
            print(r1)
            output = buf.getvalue()
        res = "[Rectangle] (12) 2/1 - 4/6\n"
        self.assertEqual(output, res)

    def test_7(self):
        """tests method display with x and y"""
        r1 = Rectangle(2, 3, 2, 2)
        output = ""
        with io.StringIO() as buf, redirect_stdout(buf):
            r1.display()
            output = buf.getvalue()
        res = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(output, res)

    def test_8(self):
        """Testing update"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.id, 89)
        r1.update(89, 2)
        self.assertEqual(r1.width, 2)
        r1.update(89, 2, 3)
        self.assertEqual(r1.height, 3)
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.x, 4)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.y, 5)

    def test_81(self):
        """update errors"""
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError) as x:
            r1.update(50, "hi")
        self.assertEqual("width must be an integer", str(x.exception))
        with self.assertRaises(ValueError) as x:
            r1.update(50, 7, 8, -1)
        self.assertEqual("x must be >= 0", str(x.exception))

    def test_9(self):
        """update with kwargs"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(r1.height, 1)
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.y, 3)

    def test_91(self):
        """update with kwargs and args"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(10, 2, width=10)
        self.assertEqual(r1.width, 2)

    def test_92(self):
        """update with kwarg errors"""
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError) as x:
            r1.update(width="hi")
        self.assertEqual("width must be an integer", str(x.exception))

    def test_13(self):
        """test to dictionary"""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        dictz = {'x': 1, 'y': 9, 'id': r1.id, 'height': 2, 'width': 10}
        self.assertEqual(r1_dictionary, dictz)
        r_dictionary = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(len(r1_dictionary), len(r_dictionary))
        self.assertEqual(type(r1_dictionary), dict)
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        r2_dictionary = r2.to_dictionary()
        self.assertEqual(len(r1_dictionary), len(r2_dictionary))
        self.assertEqual(type(r2_dictionary), dict)
        self.assertFalse(r1 == r2)

    def test_13_1(self):
        """Test for public method to_dictionary with wrong args"""

        s = "to_dictionary() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(10, 2, 1, 9)
            r1_dictionary = r1.to_dictionary("Hi")
        self.assertEqual(s, str(x.exception))


if __name__ == '__main__':
    unittest.main()

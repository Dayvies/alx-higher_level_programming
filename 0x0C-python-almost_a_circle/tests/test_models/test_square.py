"""Unittest for the base.py rectangle module
"""

import unittest
import sys
import io
from models.square import Square
from contextlib import redirect_stdout


class square_test(unittest.TestCase):
    """A TestCase for square class"""

    def test_10(self):
        """Test Square Build"""
        s1 = Square(5, 7, 8)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 7)
        self.assertEqual(s1.y, 8)
        self.assertEqual(s1.area(), 25)

    def test_101(self):
        """Test Square print"""
        s1 = Square(4)
        output = ""
        with io.StringIO() as buf, redirect_stdout(buf):
            s1.display()
            output = buf.getvalue()
        res = "####\n####\n####\n####\n"
        self.assertEqual(output, res)

    def test_102(self):
        """Test Square __str__"""
        s1 = Square(3, 10, 30)
        output = ""
        with io.StringIO() as buf, redirect_stdout(buf):
            print(s1)
            output = buf.getvalue()
        res = "[Square] ({}) 10/30 - 3\n".format(s1.id)
        self.assertEqual(output, res)

    def test_11(self):
        """Test Square error width first"""
        with self.assertRaises(TypeError) as x:
            s1 = Square("hey", 10, 10)
        self.assertEqual("width must be an integer", str(x.exception))

    def test_12(self):
        """Square Update tests"""
        s1 = Square(5)
        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.width, 2)
        self.assertEqual(s1.height, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)
        self.assertEqual(s1.id, 1)
        s1.update()
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)
        self.assertEqual(s1.id, 1)

    def test_121(self):
        """Test Square update with kwargs"""
        s1 = Square(5)
        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.width, 7)
        self.assertEqual(s1.y, 1)
        self.assertEqual(s1.id, 89)
        with self.assertRaises(TypeError) as x:
            s1.update(size="hey", id=89, y=1)
        self.assertEqual("width must be an integer", str(x.exception))

    def test_14(self):
        """Test to_dictionary square"""
        s1 = Square(10, 2, 1)
        dicz = {'id': s1.id, 'x': 2, 'size': 10, 'y': 1}
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(dicz, s1_dictionary)
        self.assertEqual(type(s1_dictionary), dict)

    def test_13_1(self):
        """Test for public method to_dictionary with wrong args"""

        s = "to_dictionary() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as x:
            s1 = Square(10, 1, 9)
            r1_dictionary = s1.to_dictionary("Hi")
        self.assertEqual(s, str(x.exception))

#!/usr/bin/python3
"""
Contains an empty class BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    About squares inherits rectangle
    """

    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    def __str__(self):
        """
        String representation of class
        """
        st = "[Square] "
        st += str(self._Rectangle__height)
        st += '/'
        st += str(self._Rectangle__height)
        return st

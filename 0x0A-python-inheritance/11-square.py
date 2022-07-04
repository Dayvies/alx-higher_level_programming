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
        """
        Initializes a square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        String representation of class
        """
        st = "[Square] "
        st += str(self._Rectangle__height)
        st += '/'
        st += str(self._Rectangle__height)
        return st

    def area(self):
        """Computes the area of a Square instance.
        Overwrites the area() method from Rectangle.
        """

        return self.__size ** 2

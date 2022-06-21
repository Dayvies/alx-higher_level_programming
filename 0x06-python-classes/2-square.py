#!/usr/bin/python3
"""
This module creates a class called square.
Private instance attribute: size
"""


class Square:
    """
    An empty class that defines a square
    Attributes:
        __size
    """

    def __init__(self, size=0):
        """
        __init__ method , during initialisation
        Args:
                size (int) : private size of square default value of 0.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

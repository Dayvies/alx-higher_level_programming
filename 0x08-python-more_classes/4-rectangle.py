#!/usr/bin/python3
"""Module 1-rectangle
Defines a Rectangle class.
"""


class Rectangle:
    """Rectangle class defined by width and height."""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance.
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of a Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a Rectangle instance
        Args:
            value: value of the width, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of a Rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle instance
        Args:
            value: value of the height, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns Area of rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Returns Perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2
    def __str__(self):
        """
        string representation of rectangle
        """
        str1 = ""
        if self.__width == 0 or self.__height == 0:
            return str1
        for j in range(self.__height):
                for x in range(self.__width):
                        str1 += '#'
                str1+='\n'
        return str1[:-1]
    def __repr__(self):
        """Return a string representation of a Rectangle instance
        that is able to recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
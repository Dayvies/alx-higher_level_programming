#!/usr/bin/python3
"""Module that creates a Rectangle"""

from models.base import Base


class Rectangle(Base):
    """Class that creates Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes class when called"""
        super().__init__(id)
        self.validator(width, "width")
        self.validator(height, "height")
        self.validator(x, "x")
        self.validator(y, "y")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """used to get the width"""
        return self.__width

    @width.setter
    def width(self, newWidth):
        """Used to set new width"""
        self.validator(newWidth, "width")
        self.__width = newWidth

    @property
    def height(self):
        """used to get the height"""
        return self.__height

    @height.setter
    def height(self, newheight):
        """Used to set new height"""
        self.validator(newheight, "height")
        self.__height = newheight

    @property
    def x(self):
        """used to get x"""
        return self.__x

    @x.setter
    def x(self, newx):
        """Used to set new x"""
        self.validator(newx, "x")
        self.__x = newx

    @property
    def y(self):
        """used to get y"""
        return self.__y

    @y.setter
    def y(self, newy):
        """Used to set new y"""
        self.validator(newy, "y")
        self.__y = newy

    def validator(self, value, name):
        """validates values"""
        n = name
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if (n == "height" or n == "width") and value <= 0:
            raise ValueError("{} must be > 0".format(n))
        if (n == "x" or n == "y") and value < 0:
            raise ValueError("{} must be >= 0".format(n))

    def area(self):
        """calculates area of rectangle"""
        return self.__height * self.__width

    def display(self):
        """prints rectangle"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print("{}{}".format(' ' * self.__x, '#' * self.__width))
        return True

    def __str__(self):
        """allows the class to be printed"""
        str1 = ("[Rectangle] ({}) {}/{}".format(self.id, self.__x, self.__y))
        str2 = (" - {}/{}".format(self.__width, self.__height))
        return (str1 + str2)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        count = 0
        for i in args:
            if count == 0:
                if i is not None:
                    self.id = i
            elif count == 1:
                self.validator(i, "width")
                self.__width = i
            elif count == 2:
                self.validator(i, "height")
                self.__height = i
            elif count == 3:
                self.validator(i, "x")
                self.__x = i
            elif count == 4:
                self.validator(i, "y")
                self.__y = i
            count += 1
        if args is not None and len(args) >= 1:
            return
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "id" and value is not None:
                    self.id = value
                    continue
                if ("_Rectangle__"+key) in self.__dict__:
                    self.validator(value, key)
                    dic_add = {("_Rectangle__"+key): value}
                    self.__dict__.update(dic_add)

    def to_dictionary(self):
        """represent in dictionary"""
        dict2 = self.__dict__.copy()
        dictdel = []
        for key in dict2.keys():
            if "_Rectangle__" in key:
                dictdel.append(key)
        for key in dictdel:
            dict2[key[12:]] = dict2.get(key)
            del dict2[key]
        return(dict2)

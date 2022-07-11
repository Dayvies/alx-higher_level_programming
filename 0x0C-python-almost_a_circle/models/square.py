#!/usr/bin/python3
"""inherits from rectangle, same width and length"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """represents a square from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes when new class is declared"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """square details in string"""
        x = self._Rectangle__x
        y = self._Rectangle__y
        s = self._Rectangle__height
        str = "[Square] ({}) {}/{} - {}".format(self.id, x, y, s)
        return str

    @property
    def size(self):
        """returns the size of square"""
        return self._Rectangle__height

    @size.setter
    def size(self, size):
        """sets the size of square"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """updates using rectangle update"""
        count = 0
        if len(args) == 1:
            if args[0] is not None:
                self.id = args[0]
            return
        elif len(args) >= 2:
            arg = args[:2]+args[1:]
            super().update(*arg)
            return
        if kwargs is not None:
            if "size" in kwargs:
                kwargs["width"] = kwargs.get('size')
                kwargs["height"] = kwargs.get('size')
            super().update(**kwargs)

    def to_dictionary(self):
        """represent the to_dictionary of square"""
        dictsq = super().to_dictionary()
        if "height" in dictsq:
            dictsq["size"] = dictsq.get("height")
            del dictsq["height"]
            del dictsq["width"]
        return dictsq

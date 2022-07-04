#!/usr/bin/python3
"""
Interchanges equal sign of int
"""


class MyInt(int):
    def __eq__(self, other):
        """
        Inverted not equals
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverted equals
        """
        return not self.__eq__(other)

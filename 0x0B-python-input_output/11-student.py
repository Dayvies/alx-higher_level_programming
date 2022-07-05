#!/usr/bin/python3
"""Student class to dict"""


class Student():
    """A class of students"""

    def __init__(self, first_name, last_name, age):
        """Initializes class student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Obtain json representation of class"""
        dict2 = self.__dict__.copy()
        if attrs == None or len(attrs) < 1:
            return dict2
        for key in attrs:
            if (type(key) != str):
                return dict2
        delKey = []
        for key in dict2.keys():
            if key in attrs:
                pass
            else:
                delKey.append(key)
        for key in delKey:
            del dict2[key]
        return dict2

    def reload_from_json(self, json):
        """ that replaces all attributes of the Student instance"""
        for key in json.keys():
            if key in self.__dict__:
                dic_add = {key: json[key]}
                self.__dict__.update(dic_add)

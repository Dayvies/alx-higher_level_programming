#!/usr/bin/python3
"""Module that creates a rectangle"""
import json
import os.path
import csv
from re import L


class Base():
    """Class that creates a base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Runs when an instance is initialised"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """json to string """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if (type(list_dictionaries) != list or
           not all(type(x) == dict for x in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes text to a file the json"""
        z = []
        if list_objs is None:
            list_objs = []
        for x in list_objs:
            y = x.to_dictionary()
            z.append(y)
        filename = "{}.json".format(cls.__name__)
        text = Base.to_json_string(z)
        with open(filename, mode='w', encoding='utf-8') as fil:
            x = fil.write(text)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes to a csv file"""
        filename = "{}.csv".format(cls.__name__)
        if cls.__name__ == "Rectangle":
            info = ["id", "width", "height", "x", "y"]
        elif cls.__name__ == "Square":
            info = ["id", "size", "x", "y"]
        else:
            return
        if (type(list_objs) != list and
           list_objs is not None or
           not all(isinstance(x, cls) for x in list_objs)):
            raise TypeError("list_objs must be a list of instances")
        z = []
        for x in list_objs:
            y = x.to_dictionary()
            z.append(y)
        with open(filename, mode='w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=info)
            writer.writeheader()
            writer.writerows(z)

    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == '':
            return []
        else:
            if type(json_string) != str:
                raise TypeError("json_string must be a string")
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            x = cls(1, 1)
        elif cls.__name__ == "Square":
            x = cls(1)
        else:
            return
        x.update(**dictionary)
        return x

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        instList = []
        filename = "{}.json".format(cls.__name__)
        fileExists = os.path.exists(filename)
        if not fileExists:
            return instList
        with open(filename, mode='r', encoding='utf-8') as fil:
            text = fil.read()
        dictList = cls.from_json_string(text)
        for x in dictList:
            y = cls.create(**x)
            instList.append(y)
        return instList

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV"""
        instList = []
        filename = "{}.csv".format(cls.__name__)
        fileExists = os.path.exists(filename)
        if not fileExists:
            return instList
        dictList = []
        with open(filename, mode='r') as fil:
            reader = csv.DictReader(fil)
            dictList = list(reader)
        for x in dictList:
            for key, value in x.items():
                try:
                    newV = int(value)
                    dic_add = {key: newV}
                    x.update(dic_add)
                except Exception:
                    pass
            y = cls.create(**x)
            instList.append(y)
        return instList

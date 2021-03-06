#!/usr/bin/python3
"""base info"""
import json


class Base:
    """info for my models"""

    __nb_objects = 0

    def __init__(self, id=None):
        """make a base model"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """"returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file:"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as JFile:
            if list_objs is None:
                JFile.write("[]")
            else:
                dir_list = [x.to_dictionary() for x in list_objs]
                JFile.write(Base.to_json_string(dir_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                it = cls(1, 1)
            else:
                it = cls(1)
            it.update(**dictionary)
            return it

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as JFile:
                dir_list = Base.from_json_string(JFile.read())
                return [cls.create(**x) for x in dir_list]
        except FileNotFoundError:
            return []

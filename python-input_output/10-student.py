#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, keys=[]):
        """return json data of object"""

        new_dict = {}
        for key in keys:
            if self.__dict__.get(key, None):
                new_dict[key] = self.__dict__.get(key)
        return new_dict if new_dict else self.__dict__

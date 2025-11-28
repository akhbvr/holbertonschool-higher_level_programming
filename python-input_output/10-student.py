#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return json data of object"""

        is_valid_attrs = isinstance(attrs, list) and \
                all(isinstance(x, str) for x in attrs)
        if is_valid_attrs:
            result = {}
            for key in attrs:
                if key in self.__dict__:
                    result[key] = self.__dict__[key]
            return result
        return self.__dict__

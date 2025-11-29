#!/usr/bin/python3
"""Pickling Custom Classes"""


import pickle


class CustomObject:
    """Custom class"""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """print out the object’s attributes"""

        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """serialize the current instance of the object"""

        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """load and return an instance"""

        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None

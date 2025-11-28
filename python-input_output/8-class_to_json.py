#!/usr/bin/python3
"""Class to JSON"""


FirstClass = __import__('8-my_class').MyClass
SecondClass = __import__('8-my_class_2').MyClass


def class_to_json(obj):
    """class to json"""

    if isinstance(obj, FirstClass) or isinstance(obj, SecondClass):
        return obj.__dict__

    return

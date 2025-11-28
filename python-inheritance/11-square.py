#!/usr/bin/python3
"""Improve Geometry"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Rectangle"""

    def __init__(self, size):
        """define width and height of rectangle"""

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """calculate rectangle area"""

        return self.__size ** 2

    def __str__(self):
        """override str method"""

        return "[Square] {}/{}".format(self.__size, self.__size)

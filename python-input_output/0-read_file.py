#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """Read file"""

    with open(filename, "r") as f:
        content = f.read()
        print(content, end="")

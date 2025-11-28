#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """append to a file"""

    with open(filename, "a") as f:
        f.write(text)
        return len(text)

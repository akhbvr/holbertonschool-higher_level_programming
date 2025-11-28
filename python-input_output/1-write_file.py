#!/usr/bin/python3
"""Write to a file"""


def write_file(filename="", text=""):
    """write to a file"""

    with open(filename, "w") as f:
        f.write(text)
        return len(text)

#!/usr/bin/python3
"""Create object from a JSON file"""


import json


def load_from_json_file(filename):
    """create object from a json file"""

    with open(filename, "r") as f:
        data = json.load(f)
        return data

#!/usr/bin/python3
"""Converting CSV Data to JSON Format"""


import csv
import json


def convert_csv_to_json(filename):
    """that takes the CSV filename as its parameter and writes the JSON data to data.json"""

    try:
        with open(filename, "r", newline="") as f:
            dict_read = csv.DictReader(f)
            rows = list(dict_read)
            with open("data.json", "w") as jf:
                json.dump(rows, jf)
            return True
    except Exception:
        return False

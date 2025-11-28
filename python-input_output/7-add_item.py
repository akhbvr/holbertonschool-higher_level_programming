#!/usr/bin/python3
"""Load, add, save"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


arguments = sys.argv[1:]

try:
    prev_data = load_from_json_file("add_item.json")
except Exception as e:
    prev_data = []
finally:
    save_to_json_file(prev_data + arguments, "add_item.json")

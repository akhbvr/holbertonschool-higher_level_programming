#!/bin/usr/python3
def element_at(my_list: list, idx: int):
    if idx < 0 and (len(my_list) - 1) < idx:
        return None
    return my_list[idx]

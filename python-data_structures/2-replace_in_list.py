#!/usr/bin/python3
def replace_in_list(my_list: list, idx: int, new_element: int):
    if idx < 0 or (len(my_list) - 1) < idx:
        return my_list
    my_list[idx] = new_element
    return my_list

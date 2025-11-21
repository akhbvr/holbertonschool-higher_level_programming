#!/usr/bin/python3
def new_in_list(my_list: list, idx: int, new_element: int):
    new_list = my_list.copy()
    if idx < 0 or (len(new_list) - 1) < idx:
        return new_list
    new_list[idx] = new_element
    return new_list

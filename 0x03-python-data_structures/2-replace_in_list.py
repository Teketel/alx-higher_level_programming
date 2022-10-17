#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    l_length = len(my_list)
    if idx < 0 or idx > l_length - 1:
        return None
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list

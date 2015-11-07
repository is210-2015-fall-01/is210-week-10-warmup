#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Using iteritems to sum a list of integers."""


DATA = {
    1: 5,
    2: 10,
    3: 15,
    4: 20,
    5: 25,
    6: 30,
    7: 35,
    8: 40,
    9: 45,
    10: 50
}


def iter_dict_funky_sum(num_list):
    """This function will sum a list.

    Args:
        It takes one argument; num_list

    Returns:
        An integer

    Examples:
        >>>
        1925
    """
    the_sum = 0
    for key_item, value_item in num_list.iteritems():
        the_sum = (value_item * key_item)+ the_sum  
    return the_sum

print iter_dict_funky_sum(DATA)

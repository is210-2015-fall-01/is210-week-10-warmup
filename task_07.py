#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for task_07"""

DATA = {
    1: 34,
    2: 45,
    3: 66,
    4: 78,
    5: 565,
    6: 523,
    7: 5464,
    8: 980,
    9: 343,
    10: 87687
}

def iter_dict_funky_sum(data):
    """This function gives you a total from a data set.

    Arg:
        data(int): numbers

    Return:
        returns the sum of the data.

    Examples:
        >>> import task_07
        >>> task_07.iter_dict_funky_sum(task_07.DATA)
        95730
    """

    total = 0
    for key, value in data.iteritems():
        total += value - key
    return total
    

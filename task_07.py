#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Iterates through a dictionary object into key and value pairs."""


DATA = {
    2: 12335,
    76: 23454657,
    3: 23454776,
    90: 345564,
    82: 234,
    45: 546,
    10: 876,
    0: 987,
    -15: 3457,
    -56: 3476,
    67: 51787
}
def iter_dict_funky_sum(data):
    """This function assigns and appends product minus key. Give total.

    Args:
        DATA(dict): assign key and value pair

    Returns:
        A funky sum.
        
    Examples:
        >>> iter_dict_funky_sum(DATA)
        47328391
    """
    total = 0
    for key, value in data.iteritems():
        total += (value - key)
    return total
    

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Function and dictionary"""

DATA = {
    1: 11,
    2: 22,
    3: 33,
    4: 44,
    5: 55,
    6: 66,
    7: 77,
    8: 88,
    9: 99,
    10: 100
    }


def iter_dict_funky_sum(dict1):
    """Adds up keys and variables in dictionary containing all integers.
    Args:
        dict1 (dict): dict containting integers for all keys and values
    Returns:
        total product of each variable minus the key, added to each other set
    Examples:
        iter_dict_funky_sum(DATA)
        >>>540
    """
    funky_total = 0
    for key, value in DATA.iteritems():
        dict1 = value - key
        funky_total += dict1

    return funky_total

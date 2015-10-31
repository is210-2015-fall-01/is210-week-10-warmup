#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""key value pairs"""

DATA = {
    2: 4,
    4: 8,
    6: 12,
    8: 16,
    10: 20,
    12: 24,
    14: 28,
    16: 32,
    18: 36,
    20: 40,
    22: 44,
    24: 48,
    }


def iter_dict_funky_sum():
    """Explaining the function inter_dict_funky_sum.
    Args:
        (dict):A dictionary of keys and values.
    Returns:
        Total of the values
    Examples:
        >>> import task_07
        >>> task_07.iter_dict_funky_sum(task_07.DATA)
        140166242
    """
    total = 0
    for key, val in DATA.iteritems():
        total += val - key
        return total

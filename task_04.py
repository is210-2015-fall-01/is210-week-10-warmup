#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Merging dictionary data."""


import data

NEWDICT = {
    'Buckingham Nicks': {
        'Lindsey Buckingham': ['guitar', 'vocals'],
        'Stevie Nicks': ['vocals', 'tambourine']
    }
}

data.BANDS.update(NEWDICT)
data.BANDS['Fleetwood Mac'].update(data.BANDS['Buckingham Nicks'])

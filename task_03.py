#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Adding to and removing from a dict copy"""


import data

CORRECTED = data.BANDS.copy()

CORRECTED['Dylan'] = {'Bob Dylan': ['vocals', 'guitar', 'harmonica']}

del CORRECTED['Van Halen']['David Lee Roth']
CORRECTED['Van Halen']['Sammy Hager'] = ['vocals']

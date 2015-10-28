#!user/bin/env python
# -*- coding: utf-8 -*-
"""Keys"""

import data

CORRECTED = data.BANDS.copy()

DYLITEM = dict([('Bob Dylan', ['vocals', 'guitar', 'harmonica'])])
CORRECTED['Dylan'] = (DYLITEM)

# CORRECTED['Dylan'] = {'Bob Dylan': ['vocals', 'guitar', 'harmonica']}

del CORRECTED['Van Halen']['David Lee Roth']

CORRECTED['Van Halen']['Sammy Hagar'] = ['vocals']

# CORRECTED['Van Halen'] = (['Sammy Hagar'], 'vocals')

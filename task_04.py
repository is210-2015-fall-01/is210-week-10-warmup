#!user/bin/env python
# -*- coding: utf-8 -*-
"""Update"""

import data

BANDS = data.BANDS
UPDATE_LIST = {'Buckingham Nicks': {'Lindsey Buckingham': ['guitar', 'vocals'],
                                    'Stevie Nicks': ['vocals', 'tambourine']}}

BANDS.update(UPDATE_LIST)

BNITEMS = BANDS['Buckingham Nicks'].items()
BANDS['Fleetwood Mac'].update(BNITEMS)

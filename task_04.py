# usr/bin/env/python
# -*- coding: utf-8 -*-
"""Updating dictionaries"""

import data

data.BANDS.copy()
data.BANDS['Buckingham Nicks'] = {'Lindsey Buckingham':['guitar', 'vocals'], 
                                  'Stevie Nicks':['vocals', 'tambourine']}

data.BANDS['Fleetwood Mac'].update(data.BANDS['Buckingham Nicks'])

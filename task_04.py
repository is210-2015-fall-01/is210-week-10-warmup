#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week10 warmup task_04."""

import data

data.BANDS.update({
    'Buckingham Nicks': {
        'Lindsey Buckingham': ['guitar', 'vocals'],
        'Stevie Nicks': ['vocals', 'tambourine'],
        }
    })
data.BANDS['Fleetwood Mac'].update(data.BANDS['Buckingham Nicks'])

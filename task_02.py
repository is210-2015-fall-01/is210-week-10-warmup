#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""How to access dictionary items."""


import data

NIGEL = data.BANDS['Spinal Tap']['Nigel Tufnel']  # copies mutable list values

# Or use: NIGEL = data.BANDS['Spinal Tap'].copy().pop('Nigel Tufnel')

BAND_NAMES = data.BANDS.keys()

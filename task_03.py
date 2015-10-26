#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Wk10 warmup task03."""

import data

CORRECTED = data.BANDS.copy()

CORRECTED['Dylan'] = {'Bob Dylan': ['Vocals', 'Guitar', 'harmonica']}

del CORRECTED['Van Halen']['David Lee Roth']

CORRECTED['Van Halen']['Sammy Hagar'] = ['Vocals']

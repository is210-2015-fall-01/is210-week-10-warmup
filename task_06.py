#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""WK10 warmup Task06."""


import data

SUPER_SIDEKICKS = {}
for HERO, HERO_DATA in data.SUPERHEROES.iteritems():
    SUPER_SIDEKICKS[HERO] = HERO_DATA.get('pet')

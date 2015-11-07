#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Changes dictionary vaales (Like assignning)."""


import data


data.SUPERHEROES.copy()['Logan']['alias'] = 'Wolverine'

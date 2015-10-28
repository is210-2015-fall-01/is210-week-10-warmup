#!user/bin/env python
# -*- coding: utf-8 -*-
"""Chang dict value"""

import data

data.SUPERHEROES.copy()['Logan']['alias'] = 'Wolverine'

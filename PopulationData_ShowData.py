#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 12:15:31 2022

@author: jajayu
"""

import pandas as pd

data = pd.read_csv('hualien.csv')
target = pd.DataFrame(data[['年度','總人口數','平地原住民','山地原住民']])
target = target.set_index(target['年度'])
target = target.drop(['年度'], axis=1)
print(target)
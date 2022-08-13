#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 05:17:01 2022

@author: jajayu
"""

import pandas as pd
data = pd.read_excel('election_2018.xls')
data.info()
print(data.head(10))
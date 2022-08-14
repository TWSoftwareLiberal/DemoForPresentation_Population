#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 11:52:40 2022

@author: jajayu
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set()
data = pd.read_csv('http://opendataap2.hl.gov.tw/resource/files/2019-03-15/b926a88f68cf8f8f478b0d2f5ac98ac4.csv')
#data = pd.read_csv('hualien.csv')

print(data)
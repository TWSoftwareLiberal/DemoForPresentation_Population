#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 14:00:22 2022

@author: jajayu
"""
import pandas as pd

data = pd.read_excel('election_2018.xls')
target = data.fillna(method='ffill')
target = target[['地區','姓名','出生年次','推薦政黨','得票數']]
target['年齡'] = 2018-target['出生年次']
target = target.drop('出生年次', axis=1)
#已指定標籤作為序列標準
#嘗試將.set_indeex()裡的順序調換
target = target.set_index(['地區', '推薦政黨']).sort_index()
print(target)
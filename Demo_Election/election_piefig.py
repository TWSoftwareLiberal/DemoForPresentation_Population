#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 14:09:57 2022

@author: jajayu
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#中文字型設定
plt.rcParams['font.sans-serif'] = [u'SimHei']
sns.set_style("darkgrid",{"font.sans-serif":[u'SimHei', 'Arial']})

#讀取檔案
data = pd.read_excel('election_2018.xls')
target = data.fillna(method='ffill')
#將所需資料過濾並加總
target = target[['推薦政黨','得票數']].groupby(by = '推薦政黨')['得票數'].sum()
target.plot.pie(y='推薦政黨')
print(target)
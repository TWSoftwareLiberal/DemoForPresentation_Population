#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 13:15:00 2022

@author: jajayu
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.font_manager import _rebuild
_rebuild()
plt.rcParams['font.sans-serif'] = [u'SimHei']
sns.set_style("darkgrid",{"font.sans-serif":[u'SimHei', 'Arial']})

data = pd.read_csv('hualien.csv')
target = pd.DataFrame(data[['年度','總人口數','平地原住民','山地原住民']])
target = target.set_index(target['年度'])
#設定圖表所需資料
fig1 = target.drop(['年度'], axis=1)
fig2 = target.drop(['年度', '總人口數'], axis=1)
#設定圖表參數
fig1.plot(ylim=(0,400000))
fig2.plot.bar(ylim=(0,80000))
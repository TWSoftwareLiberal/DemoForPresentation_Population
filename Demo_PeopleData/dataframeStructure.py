#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 10:24:57 2022

@author: jajayu
"""
from tabulate import tabulate
import pandas as pd
names = ['Alice', 'Bob', 'Cathy', 'Danny', 'Ella', 'Fiona', 'George']
score1 = [45, 67, 85, 66, 98, 78, 69]
score2 = [72, 85, 84, 68, 87, 90, 99]
score3 = [65, 84, 74, 65, 84, 88, 80]
data = pd.DataFrame([names, score1, score2, score3])

print(tabulate(data,headers='firstrow', numalign= 'left', maxcolwidths=[None, 5]))
# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2020/2/13 15:32'
import pandas as pd
df=pd.read_csv(r'cdresult.csv',engine='python',sep=',',encoding="utf_8_sig")
print(df['join_count_o'].sum())
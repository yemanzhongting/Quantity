# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2020/2/13 14:43'
import math
import pandas as pd
def getDegree(latA, lonA, latB, lonB):
    """
    Args:
        point p1(latA, lonA)
        point p2(latB, lonB)
    Returns:
        bearing between the two GPS points,
        default: the basis of heading direction is north
    """
    radLatA = math.radians(latA)
    radLonA = math.radians(lonA)
    radLatB = math.radians(latB)
    radLonB = math.radians(lonB)
    dLon = radLonB - radLonA
    y = math.sin(dLon) * math.cos(radLatB)
    x = math.cos(radLatA) * math.sin(radLatB) - math.sin(radLatA) * math.cos(radLatB) * math.cos(dLon)
    brng = math.degrees(math.atan2(y, x))
    brng = (brng + 360) % 360
    return brng

df_obj = pd.read_csv(r'agresult.csv',engine='python',sep=',',encoding="utf_8_sig")
df_bj=pd.read_csv(r'cdresult.csv',engine='python',sep=',',encoding="utf_8_sig")
all_af=df_obj['angle'].values
num_ag=df_bj['join_count_o'].values
angle=(all_af/num_ag)

data=pd.DataFrame({'angle':angle.tolist()})
data.to_csv('angle.csv',encoding="utf_8_sig")
#print(getDegree( 20, 110,20, 120))

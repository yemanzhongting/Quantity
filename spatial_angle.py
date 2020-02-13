# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/8/28 17:18'
import time,pandas
import pandas as pd
import math
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

#坐标范围，30.529114-30.809326,103.894287-104.234131共计2500个格子
Y1=30.529114
Y2=30.809326
X1=103.894287
X2=104.234131
N=20
x_gap=(X2-X1)/N
y_gap=(Y2-Y1)/N

#经度间隔 0.4767285017325457km
#纬度间隔  0.6220706399999973km

index_all=N*N

def get_mn(X,Y):
    #利用地板除，刚好返回他们的索引，这样就可以,索引以0开始
    m=(X-X1)//x_gap
    n=(Y-Y1)//y_gap
    #print(m,n)
    index=(n)*20+m+1
    return index

with open(r'C:\Users\hp\Desktop\成都\Argis_python\order_20161101.csv','r+',encoding='utf-8') as f:
    tmp=f.readlines()

all_rows=len(tmp)-1
print(all_rows)

data = {'gridid': [i+1 for i in range(index_all)],
        'join_count_o':[0 for i in range(index_all)],
        'join_count_d':[0 for i in range(index_all)],
        'time_sum':[0 for i in range(index_all)],
        'angle':[0 for i in range(index_all)]
        }
df = pd.DataFrame(data)

print(df)
print(df.size)

# with open('order_20161101_w.csv','w+',encoding='utf-8') as f:  getDegree
for i in range(len(tmp)-1):
    i=i+1
    # print(i)
    tmp_list=tmp[i].split(',')

    tmp_time=0#(int(tmp_list[2])-int(tmp_list[1]))/60#以分钟计时

    tmp_oX=float(tmp_list[3])
    # print(tmp_oX)
    tmp_oY=float(tmp_list[4])
    tmp_dX =float(tmp_list[5])
    tmp_dY =float(tmp_list[6])

    #还需要判断是否在方格内
    #步骤1 计算O
    if tmp_oX>X1 and tmp_oY>Y1:
        if tmp_oX<X2 and tmp_oY<Y2:
            if tmp_dX > X1 and tmp_dY > Y1:
                if tmp_dX < X2 and tmp_dY < Y2:
                    tmp_index=int(get_mn(tmp_oX,tmp_oY))
                    tmp_index_d =int(get_mn(tmp_dX, tmp_dY))

                    df.iloc[tmp_index-1, 4]=df.iloc[tmp_index-1,4]+getDegree(tmp_oY,tmp_oX,tmp_dY,tmp_dX,)#(latA, lonA, latB, lonB)
                    df.iloc[tmp_index-1, 3] =df.iloc[tmp_index-1,3]+tmp_time
                    #该坐标出发网格，打车时间总计
                    df.iloc[tmp_index-1, 1] =df.iloc[tmp_index-1,1]+1
                    #该坐标出发网格count+1
                    df.iloc[tmp_index_d-1, 2] =df.iloc[tmp_index_d-1,2]+1
                    #该行车记录抵达的坐标网格 count+1

# header: 是否保存列名，默认为
# True ，保存
# index: 是否保存索引，默认为
# True ，保存

df.to_csv(r'agresult.csv', sep=',',header=True, index=False)

print('ok!')





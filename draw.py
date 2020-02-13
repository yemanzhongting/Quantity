# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2020/2/13 16:24'
import pandas as pd
import matplotlib.pyplot as plt
import math
from mpl_toolkits.basemap import Basemap
from pylab import *
import numpy as np

mpl.rcParams['font.sans-serif'] = ['SimHei']

# for i in range(1, 3):
#     plt.subplot(2, 1, i)
#     ax = plt.gca()
#     wind = [x for x in range(1, 9)]
#     # angle = [45*x for x in range(0,8)]
#     # lon = list(np.linspace(113.8, 114.6, 8))
#     lat = list(np.linspace(22.4, 22.85, 8))
#
#     # wind = [2]*8
#     angle = [90] * 8  # 为方便比较长度，箭头方向设置成一样
#     lon = [114.27] * 8  # 为方便比较长度，箭头经度设置成一样
#
#     # 指定地图范围、投影方式（projection）等  area_thresh是与湖泊等在地图上显示相关的参数
#     m = Basemap(llcrnrlon=113.7, llcrnrlat=22.35, urcrnrlon=114.7, urcrnrlat=22.9, \
#                 rsphere=(6378137.00, 6356752.3142), \
#                 resolution='l', area_thresh=1000., projection='lcc', lat_1=22.5, lat_0=22.5, lon_0=114, ax=ax)
#     lon, lat = m(*(lon, lat))
#
#     # 一系列的U、V
#     ver = [-spd * math.sin(math.radians(agl)) for spd, agl in zip(wind, angle)]  # U分量
#     hriz = [-spd * math.cos(math.radians(agl)) for spd, agl in zip(wind, angle)]  # V分量
#     print(ver, '\n', hriz)
#
#     ax = plt.gca()
#     # 下面两行是读取地图中的shape文件，即轮廓图
#     m.readshapefile('H:\Example\StudyAll', 'states', color='grey', )  # HongKong encoding='utf-8'
#     # # m.readshapefile(r'G:\深圳季风研究\gadm36_CHN_shp\gadm36_CHN_3', 'states',color='grey') #Mainland in given lon and lat
#     # m.readshapefile(r'G:\深圳季风研究\gadm36_sz_shp\Bon_data\xzq_sz_pop', 'states', color='grey')
#
#     m.scatter(lon, lat, s=2, color='goldenrod', marker="o")  # 根据经纬度，画出对应站点位置
#     ax.set_title('风场')
#     # ax.quiver(lon, lat, ver, hriz, units='width', scale=2, width=0.01, color='deepskyblue')
#     ax.quiver(lon, lat, ver, hriz, color='deepskyblue', width=0.005, scale=30)
#
#     for i, wspd in enumerate(wind):
#         ax.annotate(str(wspd), (lon[i], lat[i]))
#
#     # 在图上添加一些文字信息
#     plt.text(0.6, 0.9, r'$mean: $' + str(18) + '°', color='forestgreen', transform=ax.transAxes,
#              fontweight='extra bold')
#     plt.text(1.02, 0.6, r'$S: $' + str(18) + '%', color='forestgreen', transform=ax.transAxes, fontweight='heavy')
#     plt.text(1.02, 0.4, r'$N: $', color='forestgreen', transform=ax.transAxes, fontweight=100)
#
#     # 画经纬度网格
#     m.drawmeridians([114.0, 114.4], labels=[1, 0, 0, 1])  # meridian：子午线，经线 arange指明范围和间隔
#     m.drawparallels(np.arange(15, 30, 0.3), labels=[1, 0, 0, 0])  # 画纬度平行线
#
#     # 比例尺长度的U、V值和位置
#     q_lon, q_lat = m(*(114.27, 22.75))
#     spd = 2
#     angle_all = 90
#     ver_all = -spd * math.sin(math.radians(angle_all))
#     hriz_all = -spd * math.cos(math.radians(angle_all))
#     # ax.quiver(q_lon, q_lat, ver_all, hriz_all, color='g', pivot='mid') # mid是旋转枢纽在中间，默认在尾部
#     ax.quiver(q_lon, q_lat, ver_all, hriz_all, color='g', scale=30)
#
#     # 画比例尺
#     plt.text(0.82, 0.1, r'$scale:$', color='r', transform=ax.transAxes, fontweight=100, fontsize=8)
#     plt.text(0.82, 0.03, r'$2m/s$', color='r', transform=ax.transAxes, fontweight=100, fontsize=8)
#     plt.quiver(95000, 3000, 3, hriz_all, color='r', width=0.005, scale=50)
#     print(-ver_all, hriz_all)

# 这一段与画箭头不相干，可忽略注释掉  画散点,为不同散点设置不同颜色
# Colors=('#DDDDFF','#7D7DFF','#0000C6','#000079','#CEFFCE','#28FF28','#007500','#FFFF93')
# sc = plt.scatter(lon, lat, s=100, color=Colors, marker="o") #根据经纬度，画出对应站点位置
# for i,txt in enumerate(Colors):
# 	ax.annotate(txt,(lon[i],lat[i]), fontsize=5)

from matplotlib import pyplot as plt
import numpy as np

df_obj = pd.read_csv(r'细颗粒度数据.csv',engine='python',sep=',',encoding="utf_8_sig")
lng=df_obj['lng'].values.tolist()
lat=df_obj['lat'].values.tolist()
angle=df_obj['angle'].values.tolist()
class_=df_obj['modularity_class'].values.tolist()

# # 绘制曲线
# x = np.linspace(2, 21, 20)  # 取闭区间[2, 21]之间的等差数列，列表长度20
# y = np.log10(x) + 0.5
# plt.figure()  # 添加一个窗口。如果只显示一个窗口，可以省略该句。
# plt.plot(x, y)  # plot在一个figure窗口中添加一个图，绘制曲线，默认颜色

# 绘制离散点
# plt.plot(lng, lat, '.y')  # 绘制黄色的点，为了和曲线颜色不一样
# x0, y0 = 15, np.log10(15) + 0.5
# plt.annotate('Interpolation point', xy=(x0, y0), xytext=(x0, y0 - 1), arrowprops=dict(arrowstyle='->'))  # 添加注释
plt.figure(figsize=(12.8,9.6))

# f, (ax1) = plt.subplots(figsize = (12.8,9.6))#,nrows=2 并列两个

for x0, y0 ,ang ,cla in zip(lng, lat,angle,class_):

    # plt.scatter(x0,y0)
    if cla==9:
        plt.quiver(x0, y0, 0, -2, color='#6a76c2', width=0.005, angles=ang)  # 绘制箭头
    elif cla==5:
        plt.quiver(x0, y0, 0, -2, color='#5ac343', width=0.005, angles=ang)
    elif cla==7:
        plt.quiver(x0, y0, 0, -2, color='#d74e2c', width=0.005, angles=ang)
    elif cla==8:
        plt.quiver(x0, y0, 0, -2, color='#c84892', width=0.005, angles=ang)
    else:
        plt.quiver(x0, y0, 0, -2, color='#000000', width=0.005, angles=ang)
    # print(x0)
    #if x0==103.9027863:


# x = range(2, 21, 5)
# y = np.log10(x) + 0.5
# plt.plot(x, y, 'om')  # 绘制紫红色的圆形的点
# x0, y0 = 7, np.log10(7) + 0.5
# plt.annotate('Original point', xy=(x0, y0), xytext=(x0, y0 - 1), arrowprops=dict(arrowstyle='->'))
# for x0, y0 in zip(x, y):
#     plt.quiver(x0, y0 + 0.3, 0, -1, color='g', width=0.005)  # 绘制箭头

# 设置坐标范围
# plt.xlim(2, 21)  # 设置x轴范围
# plt.xticks(range(0, 23, 2))  # 设置X轴坐标点的值，为[0， 22]之间的以2为差值的等差数组
# plt.ylim(0, 3)  # 设置y轴范围

# 显示图形

# ax1.set_xlabel('lng')
#
# #ax1.set_xticklabels([]) #设置x轴图例为空值
#
# ax1.set_ylabel('lat')
plt.ylabel('Lat', fontdict={'family' : 'Times New Roman', 'size'   : 16})
plt.xlabel('Lng', fontdict={'family' : 'Times New Roman', 'size'   : 16})
plt.yticks(fontproperties = 'Times New Roman', size = 14)
plt.xticks(fontproperties = 'Times New Roman', size = 14)
# plt.legend()
plt.rcParams['savefig.dpi'] = 300 #图片像素
plt.rcParams['figure.dpi'] = 300 #分辨率

plt.savefig('1.png')
plt.show()  # 显示绘制出的图




# data.to_csv('angle.csv',encoding="utf_8_sig")
#print(getDegree( 20, 110,20, 120))
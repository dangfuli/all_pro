# encoding=utf-8
import matplotlib.pyplot as plt
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']

names = ['5', '10', '15', '20', '25']
x = range(len(names))
# y = [0.855, 0.84, 0.835, 0.815, 0.81]
# y1=[0.86,0.85,0.853,0.849,0.83]
y = [1,2,3,4,5]
y1 = [1.12,2.32,3.44,4.33,5.76]


# plt.plot(x, y, 'ro-')
# plt.plot(x, y1, 'bo-')
# plt.xlim(-1, 11)  # 限定横轴的范围
# plt.ylim(-1, 110)  # 限定纵轴的范围
plt.plot(x, y, marker='.', mec='r', mfc='w',label=u'y=x^2曲线图')  #画横轴，竖轴
plt.plot(x, y1, marker='*', ms=10,label=u'y=x^3曲线图')    # 在数轴上描点
plt.legend()  # 让图例生效
plt.xticks(x, names, rotation=45)
plt.margins(0)
plt.subplots_adjust(bottom=0.15)
plt.xlabel(u"time(s)邻居") #X轴标签
plt.ylabel("RMSE") #Y轴标签
plt.title("A simple plot") #标题

plt.show()


import requests
# from bs4 import BeautifulSoup
# d = 'https://detail.tmall.com/item.htm?id\u003d544021441147\u0026ad_id\u003d\u0026am_id\u003d\u0026cm_id\u003d140105335569ed55e27b\u0026pm_id\u003d\u0026abbucket\u003d12'
# f = 'https://chaoshi.detail.tmall.com/item.htm?id=544021441147&cm_id=140105335569ed55e27b&abbucket=12'
# print(d)
# r = requests.get(d)
# print(r.url)
# print(r.text)
# #
# print('kaishi'.center(50,'*'))
# k = {'a':'1'}
# print(k.get('b'))

#! python3
# 这里放程序说明

import os, pprint, json
import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
from matplotlib import pylab, mlab

os.chdir("D:\\Project\\Python\\Data") #设置工作目录
path=r'.\ch02\usagov_bitly_data2012-03-16-1331923249.txt' #设置JSON文件
records=[json.loads(line) for line in open(path)] #JSON读取文件中的Records，读取到列表records中
print(records[0]) # 输出第1个列表
print(records[0]['tz']) # 输出第1个列表中，键为'tz'的值

# time_zones=[rec['tz'] for rec in records] #把所有tz读进time_zones，但会碰到错误，因不是每个记录都有time zone
time_zones=[rec['tz'] for rec in records if 'tz' in rec] #把所有tz读进time_zones，并规避没有time zone的记录
# print(time_zones)

#pprint
# pprint.pprint(time_zones[:10]) # 输出前10个time zone，发现有空值

#print first 10 records of time zone
for r in time_zones[:10]:
    print("'" + (r) + "'")

frame=DataFrame(records)
# print(frame) #输出frame的摘要
# print(frame['tz'].value_counts()) #对tz字段进行计数，并从大到小排列
print(frame['tz'].value_counts()[:10]) #对tz字段进行计数，并从大到小排列，并取前10个数据
print('----------------------') #在输出的部分空出一行

clean_tz=frame['tz'].fillna('Missing') #将tz中缺失的内容调整为'Missing'，并赋值给clean_tz
print(clean_tz.value_counts()[:10]) #比较一下与frame['tz']输出的结果的差异，多了一个Missing值的计数
print('----------------------') #在输出的部分空出一行

clean_tz[clean_tz=='']='Unknown' #把clean_tz中的空字符，替换为Unknown，再返回给clean_tz
print(clean_tz.value_counts()[:10]) #比较一下与前2个的差异，多了一个Unknown
print('----------------------') #在输出的部分空出一行

tz_counts=clean_tz.value_counts()
tz_counts[:10].plot(kind='barh', rot=0)
# plt.show() #此句用于在plot后显示图形
pylab.show() #此句用于在plot后显示图形, plt为定义的pylab的别名


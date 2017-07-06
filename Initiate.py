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

'''
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
tz_counts[:10].plot(kind='barh', rot=0) #定义为横向柱图
# plt.show() #此句用于在plot后显示图形
# pylab.show() #此句用于在plot后显示图形, plt为定义的pylab的别名
'''

print(frame.a.dropna()) #丢掉na值后的frame中的a字段的值
results=Series([x.split()[0] for x in frame.a.dropna()]) #分离后取第1个值，即浏览器型号，默认按空格分离
# results=Series([x.split('/')[0] for x in frame.a.dropna()]) #分离后取第1个值，即浏览器型号，按'/'分离
print(results.value_counts()[:10]) #输出计数结果中的前10个值

cframe=frame[frame.a.notnull()] #外面不套frame[]，会变成true / false值
# print(cframe)
operating_system=np.where(cframe['a'].str.contains('Windows'),'Windows','NotWindows') #根据a中是否含Windows，判断是否为Windows系统
# print(operating_system[:10])
by_tz_os=cframe.groupby(['tz',operating_system]) #根据timezone和operating_system对数据进行分组
agg_counts=by_tz_os.size().unstack().fillna(0) #size用于对分组数据进行计数，unstack用于重组数据，fillna(0)指无效数据计0
print(agg_counts[:10])
#用于按排列
indexer=agg_counts.sum(1).argsort()
count_subset=agg_counts.take(indexer)[-10:]

count_subset.plot(kind='barh', stacked=True)
pylab.show()
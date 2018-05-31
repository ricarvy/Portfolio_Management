# -*- coding: utf-8 -*-

# @Time  :2018/5/31 12:40
# @File  : featureDataMatrics.py
# @Author: LI Jiawei

import h5py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_directory = '../database/data/'
format2_list=['data_format2_20170918_20170922.h5']
              # 'data_format2_20170918_20170922.h5',
              # 'data_format2_20170925_20170929.h5',
              # 'data_format2_20171009_20171013.h5',
              # 'data_format2_20171016_20171020.h5']

def index_trasaction(df):
    df['open']=df[0]
    df['high']=df[1]
    df['low']=df[2]
    df['close']=df[3]
    df['volume']=df[4]
    df.drop([0,1,2,3,4], axis=1, inplace=True)
    return df

def format_trasaction(bdData_train,keys):
    total_list = list()
    for i in range(13):
        sample_list = list()
        for j in range(len(keys)):
            data_cur_min = bdData_train[keys[j]][i]
            sample_list.append(data_cur_min)
        total_list.append(sample_list)
    return total_list

def createDataFrame(format2_list,file_index,stock_index):
    format2_dir = format2_list[file_index]
    data_format_path = data_directory + format2_dir
    btData_train = h5py.File(data_format_path, mode='r')
    keys = list(btData_train.keys())
    data = format_trasaction(bdData_train=btData_train,keys=keys)
    series_list = []
    stock_list = data[stock_index]
    for j in range(len(stock_list)):
        series = pd.Series(np.array(stock_list[j]))
        series_list.append(series)
    df = index_trasaction(pd.DataFrame(series_list))
    return data,df, keys

data_set = []
for file_index in range(len(format2_list)):
    for stock_index in range(13):
        print(stock_index)
        data, df, keys= createDataFrame(format2_list, file_index, stock_index)
        data_set.append(df['close'])
date_set = np.arange(0, len(data_set[0]))
print('finished read!')
for i in range(13):
    plt.plot(date_set, data_set[i])
    plt.xlabel(keys[i]+'_value')
    plt.ylabel('close_price')
    plt.show()
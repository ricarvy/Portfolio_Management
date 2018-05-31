# -*- coding: utf-8 -*-

# @Time  :2018/5/31 12:18
# @File  : plot_data_trend.py
# @Author: LI Jiawei

import matplotlib.pyplot as plt

def plot(data, date):
    plt.plot(date[0], data[0])
    plt.xlabel('date')
    plt.ylabel('close_value')
    plt.show()
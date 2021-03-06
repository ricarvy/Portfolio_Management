# -*- coding: utf-8 -*-
# @Time    : 2018/3/28 20:02
# @Author  : Li Jiawei
# @FileName: environment.py
# @Software: PyCharm

import pandas as pd
import numpy as np
import time

class Environment:
    def __init__(self, config, globalDataMatrix, start, end, coin_list):

        ### the globalDataMatirx is defined as type pandas.Dataframe
        self.__data = globalDataMatrix.get_global_panel()

        ### plz use timestamp, not str
        self.__start_time = start

        ### plz use timestamp, not str
        self.__end_time = end

        self.__coin_list = coin_list

        self.__coin_num = self.get_coin_num()

        self.__period = 300

        self.__feature = 'close'

    '''
        return the price vector of each asset of time t
        
    '''
    def get_price_vector_from_t(self,t, coin_list, index):
        closes = []
        for i, coin in enumerate(coin_list):
            close = self.__data.loc[(self.__data['date'] == t) & (self.__data['coin'] == coin_list[i][0])][index]
            closes.append(close)
        return (close)
    '''
        create price relative vector(PRV)
        The format is like below:
        PRV(t)=[1,V(1,t)/V(1,t-1),V(2,t)/V(2,t-1),...V(coin_num,t)/V(coin_num,t-1)]
        
        :param
            t: 
                dtype: integer
                script: a time point from asset history data panel
        :return
            prv:
                dtype: np.ndarray, shape=(1, coin_num)
                script: the prv value of time t using the format above

     '''
    def get_y_t(self, t, coin_list):
        v_t_cur = self.get_price_vector_from_t(t, coin_list, self.__feature)
        v_t_pre = self.get_price_vector_from_t(t-self.__period, coin_list, self.__feature)

        prv=np.zeros(self.__coin_num, dtype=float)
        for i in range(self.__coin_num):
            if i == 0:
                prv[i] = 1
            else:
                prv[i] = v_t_cur[i]/v_t_pre[i]
        return prv


    def get_coin_num(self):
        return len(self.__coin_list)

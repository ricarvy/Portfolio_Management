# -*- coding: utf-8 -*-
# @Time    : 2018/3/28 20:02
# @Author  : Li Jiawei
# @FileName: environment.py
# @Software: PyCharm

import pandas as pd
import numpy as np

class Environment:
    def __init__(self, config, globalDataMatrix, start, end, coin_list):

        ### the globalDataMatirx is defined as type pandas.Dataframe
        self.__data = globalDataMatrix

        self.__start_time = start

        self.__end_time = end

        self.__coin_list = coin_list

        self.__coin_num = self.get_coin_num()

        self.__period = 300

        self.__feature = 'close'

    '''
        return the price vector of each asset of time t
        
    '''
    def get_price_vector_from_t(self,t, index):
        close=self.__data.loc[self.__data['date'] == t][index]
        return float(close)

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
    def get_y_t(self, t):
        v_t_cur = self.get_price_vector_from_t(t, self.__feature)
        v_t_pre = self.get_price_vector_from_t(t-self.__period, self.__feature)

        prv=np.zeros(self.__coin_num, dtype=float)
        for i in range(self.__coin_num):
            if i == 0:
                prv[i] = 1
            else:
                prv[i] = v_t_cur/v_t_pre
        return prv


    def get_coin_num(self):
        return len(self.__coin_list) + 1
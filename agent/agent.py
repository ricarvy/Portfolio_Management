# -*- coding: utf-8 -*-
# @Time    : 2018/3/28 19:48
# @Author  : Li Jiawei
# @FileName: agent.py
# @Software: PyCharm

import numpy as np

class Agent:
    def __init__(self, coin_list, p, environment):
        self.__name = 'nn_agent'

        self.__coin_list = coin_list

        ### initialize the weight
        ### means the ratio for each coin
        self.__weight_vector = self.weight_vector_initialization()
        self.__weight_vector_history=[self.__weight_vector]

        ### initialization of total asset
        self._p = p
        self._p_history = [p]

        ### the environment of asset
        self.__env = environment



    def weight_vector_initialization(self):
        weight_vector=[]
        for coin_num, coin in enumerate(self.__coin_list):
            if coin_num == 0:
                weight_vector.append(1)
            else:
                weight_vector.append(0)
        return weight_vector

    def calculate_return_rate(self,t,pre_way):
        y_t=self.__env.get_y_t(t)
        wv = self.__weight_vector
        current_p=self._p
        update_p = 0.0
        if(len(y_t) == len(wv)):
            for index, element in enumerate(y_t):
                update_p = update_p+ y_t[index]* wv[index]
            self._p_history.append(update_p)
        else:
            raise ValueError('The shape of y_t is not the same as wv, plz check it.')

        if (pre_way == 'ro'):
            return (update_p / current_p)-1.0
        elif (pre_way == 'r'):
            return np.log(update_p / current_p)
        else:
            return 0

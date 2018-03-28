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

        ### initialization of total asset
        self._p = p

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


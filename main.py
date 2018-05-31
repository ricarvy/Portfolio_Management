# -*- coding: utf-8 -*-
# @Time    : 2018/3/14 19:33
# @Author  : Li Jiawei
# @FileName: main.py
# @Software: PyCharm

from __future__ import division
from argparse import ArgumentParser

from model.modelGenerator import Model
from tools.config_loader import ConfigLoader
from environment.environment import Environment
from tools.time_format_transformer import timestamp2str,str2timestamp
from tools.json_loader import config_load
from  model.actor_critic import build_AC_Model
from marketData.globalDataMatrics import GlobalDataMatrics
from agent.agent import Agent
from plot.plot_data_trend import plot

import pandas as pd
import numpy as np

def parser_builder():
    parser=ArgumentParser()
    parser.add_argument("--mode",
                        dest="mode")
    parser.add_argument("--process",
                        dest="process")
    return parser

def main():
    parser=parser_builder()
    option=parser.parse_args()
    configLoader=ConfigLoader()
    config=configLoader.load_config()
    ### just a test, plz test your local function in this model !
    if option.process == 'test':
        test(config)

    if option.process == 'generate_model':
        modelGeneration(config)

def modelGeneration(config):
    print('model is generating...')
    model=Model(config)
    model=model.generateModel()

'''
Download the data matrix from external resourses

The method 
'''

'''
Prepare the basic data frame from database(like data.db)

The database is prepared in the folder 'Portfolio_Management/database'
if the folder is empty, pls run the code : 
main.py --process=databaseloader
firstly

Using this method we can get trainable dataframe

'''
def dataPreprocessing(database,):
    print('dataPreprocessing')

'''
    just a test of function
    Have fun !!!!!!!
    Enjoy yourself in this function !!!
        
'''
def test(config):
    gdm = GlobalDataMatrics(config=config,
                            start='2015-07-01',
                            end='2017-07-01')
    coin_list=gdm.get_coin_list().values
    # coin_list = [['ETH']]
    #env=Environment(config,gdm,1439010900,1439011200,coin_list)
    # result=env.get_price_vector_from_t(1439010600,index='close')
    max_date_set = []
    min_date_set = []
    # for coin in coin_list:
    #     max_Date = gdm.get_global_panel(coin = coin[0]).max(axis = 0)[0]
    #     max_date_set.append(max_Date)
    #     min_Date = gdm.get_global_panel(coin=coin[0]).min(axis=0)[0]
    #     min_date_set.append(min_Date)
    #     result = gdm.get_global_panel(coin = coin[0]).count()
    #     print('The num of record of ',coin,' is ',result[0], ' and the maxdate is ', timestamp2str(max_Date), ' and the minndate is ', timestamp2str(min_Date))

    ### 寻找公共时间序列
    # start_date = np.max(min_date_set)
    # end_date = np.min(max_date_set)
    # print('time start on ',timestamp2str(start_date), ' end on ', timestamp2str(end_date))

    ETH = gdm.get_global_panel(coin = 'ETH')
    ETH_close = ETH['close'].values
    ETH_date = ETH['date'].values
    data = [ETH_close]
    date = [ETH_date]
    plot(data,date)


    # agent = Agent(coin_list=coin_list, p=10000000, environment=env)
    # print(agent.calculate_return_rate(t=1439010900,coin_list = coin_list))
    # params = config_load(path='net_params.json')
    # online_Q_net, target_Q_net, online_tra_net, target_tra_net = build_AC_Model(coin_num=11, params=params)
    # print(online_tra_net.summary())






if __name__ == "__main__":
    # main()
    test(config=None)
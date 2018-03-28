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

import pandas as pd

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
    pass





if __name__ == "__main__":
    main()
    ### test()
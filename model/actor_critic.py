# -*- coding: utf-8 -*-

# @Time  :2018/5/31 10:47
# @File  : actor_critic.py
# @Author: LI Jiawei

from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import RMSprop

from tools.json_loader import config_load

import numpy as np

def dense_layer_gen(coin_num, params):
    model = Sequential()

    # First layer.
    model.add(Dense(
        params[0]['neuron_num'], kernel_initializer=params[0]['initializer'], input_shape=(coin_num,)
    ))
    model.add(Activation(params[0]['activation']))
    model.add(Dropout(params[0]['dropout']))

    # Second layer.
    model.add(Dense(params[1]['neuron_num'], kernel_initializer=params[1]['initializer']))
    model.add(Activation(params[1]['activation']))
    model.add(Dropout(params[1]['dropout']))

    # Output layer.
    model.add(Dense(params[2]['neuron_num'], kernel_initializer=params[2]['initializer']))
    model.add(Activation(params[2]['activation']))

    rms = RMSprop()
    model.compile(loss='mse', optimizer=rms)
    return model

def build_AC_Model(coin_num, params):
    online_Q_net = dense_layer_gen(coin_num, params['online_Q_net'])
    target_Q_net = dense_layer_gen(coin_num, params['target_Q_net'])
    online_tra_net = dense_layer_gen(coin_num, params['online_tra_net'])
    target_tra_net = dense_layer_gen(coin_num, params['target_tra_net'])

    return online_Q_net, target_Q_net, online_tra_net, target_tra_net

def test():
    test_X_data = np.random.random([2, 1, 11])
    test_y_data = np.random.random([2, 1, 11])
    params = config_load(path='../net_params.json')
    online_Q_net, target_Q_net, online_tra_net, target_tra_net = build_AC_Model(coin_num=11, params=params)
    online_Q_net.fit(x = test_X_data[0], y = test_y_data[0])


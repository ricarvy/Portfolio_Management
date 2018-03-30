# -*- coding: utf-8 -*-
# @Time    : 2018/3/29 11:51
# @Author  : Li Jiawei
# @FileName: time_format_transformer.py
# @Software: PyCharm
'''
About this module
The limit of time should be from 1970-01-01 00:00:00 to 2038-01-19 03:14:07

About the limitation, visit the following link if interestd:
Chinese Version:
http://developer.51cto.com/art/201508/488060.htm

English Version:
https://unix.stackexchange.com/questions/26205/why-does-unix-time-start-at-1970-01-01


'''
import time

'''
The function is used to transform the time str like format given: 
    YYYY-mm-DD HH:MM:SS
to the format as a timestamp with the scale 's'
like:
2015-08-08 13:15:00 -> 1439010900

Warning: the return value type must be integer !
According to the database
date(INTEGER)

'''
def str2timestamp(str):
    if len(str) == 10:
        str = str+' 00:00:00'
    return int(time.mktime(time.strptime(str,'%Y-%m-%d %H:%M:%S')))


'''
The function is used to fransform timestamp to time str like format given:

1439010900 -> 2015-08-08 13:15:00 
'''
def timestamp2str(timestamp):
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(timestamp))

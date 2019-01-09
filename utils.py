#-*-coding:utf-8 -*-
#Author: Gui

import logging

def complex(amount, rate, time):
    #print('princical amount: {}'.format(amount))
    for t in range(1, time + 1):
        amount = round(amount * (rate + 1),2)
        #print('year {}: {}'.format(t, amount))
    return amount

def complex_detail(amount, rate, time):
    ret_list = []
    for t in range(1, time + 1):
        amount = round(amount * (rate + 1),2)
        ret_list.append((t,amount))
    return ret_list


def users_value(user_cnt, user_value):
    return user_cnt*user_value

def setup_logger(level=logging.DEBUG, name='__main__', rich=False):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    handler = logging.StreamHandler()
    if rich:
        formatter = logging.Formatter('[%(asctime)s] [%(threadName)s] [%(levelname)s] %(message)s')
    else:
        formatter = logging.Formatter('[%(asctime)s] %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

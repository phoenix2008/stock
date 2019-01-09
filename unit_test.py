#-*-coding:utf-8 -*-
#Author: Gui

import logging

def test_list():
    my_list = list(range(10))
    print(my_list)

def complex_detail(amount, rate, time):
    #print('princical amount: {}'.format(amount))
    ret_list = []
    for t in range(1, time + 1):
        amount = amount * (rate + 1)
        ret_list.append((t,amount))
        #print('year {}: {}'.format(t, amount))
    return ret_list


if __name__ == '__main__':
    test_list()
    result_list = complex_detail(3.5, 0.1, 5)
    print result_list

#-*-coding:utf-8 -*-
#Author: Gui
def invest(amount, rate, time):
    print('princical amount: {}'.format(amount))
    for t in range(1, time + 1):
        amount = amount * (rate + 1)
        print('year {}: {}'.format(t, amount))

invest(3.5, 0.1, 3)
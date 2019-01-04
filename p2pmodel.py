#-*-coding:utf-8 -*-
#Author: Gui

import utils
import logging
from optparse import OptionParser

logger = utils.setup_logger(name='p2pmodel')

def valuebyprofit():
    # 1, 最简单的按2018年利润，3年复合增长计算
    value_bad  = utils.complex(3.5, 0.1, 5)
    print value_bad*3

def valuebyusers():
    # 2, 按用户数计算
    #拍拍贷财报显示200万用户数
    value_good = utils.complex(200,0.05,3)
    #每用户价值=平均用户借款额*5%（利润）= 4000*5%
    logger.info( '本年利润-按用户数计算 %s' % float(200*4000*0.05))

    logger.info(value_good*4000*0.05)


def getOpt():
    parser = OptionParser()
    parser.add_option("-v", action="store_true", dest="verbose", help="run in verbose mod")
    (options, args) = parser.parse_args()


if __name__ == '__main__':
    options = getOpt()
    logger.setLevel(logging.INFO)
    valuebyprofit()
    valuebyusers()
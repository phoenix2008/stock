#-*-coding:utf-8 -*-
#Author: Gui

import utils
import logging
from optparse import OptionParser

logger = utils.setup_logger(name='p2pmodel')

'''
参数：
初始利润，年增长率，
用户数，每用户借款额，每用户借款的take rate
#新增，政策因素
'''

def valuebyprofit():
    # 1, 最简单的按2018年利润，3年复合增长计算
    list_value_good = utils.complex_detail(3.5, 0.1, 5)
    logger.info('历年利润：%s' % list_value_good)
    value_good = utils.complex(3.5, 0.1, 5)
    logger.info('2023年利润-按2018季度利润计算 %s 亿' % float(value_good))
    logger.info('市值按利润计算 %s 亿' % float(value_good*5))


def valuebyusers():
    # 2, 按用户数计算
    #拍拍贷财报显示320万单一活跃借款用户数 2018 q3, 年估计有1000万=0.1亿
    list_value_good = utils.complex_detail(0.1, 0.1, 5)
    logger.info('历年用户数：%s 亿' % list_value_good)
    value_good = utils.complex(0.1,0.1,5)
    #每用户价值=平均用户借款额*5%（利润）= 4000*5%
    value_per_user = float(4000*0.05)
    result_usd = float(value_good*value_per_user)/7
    logger.info('5年后利润-按用户数计算 %s 亿' % result_usd)

    logger.info('按用户数计算市值，5倍年利率，市值：%s 亿' % float(result_usd*5) )


def getOpt():
    parser = OptionParser()
    parser.add_option("-v", action="store_true", dest="verbose", help="run in verbose mod")
    (options, args) = parser.parse_args()


if __name__ == '__main__':
    options = getOpt()
    logger.setLevel(logging.INFO)
    valuebyprofit()
    valuebyusers()

# -*- coding:utf-8 -*-
# @FileName  :errorHandle.py
# @Time      :2022/5/11 18:28
# @Author    :dzz
# @Function  :
import logging
logging.basicConfig(level=logging.INFO)

from datetime import *

def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


if __name__ == "__main__":
    # try:
    #     print('try...')
    #     r = 10 / 0
    #     print('result:', r)
    # except ZeroDivisionError as e:
    #     print('except:', e)
    # finally:
    #     print('finally...')

    # try:
    #     bar('0')
    # except Exception as e:
    #     logging.exception(e)  # 记录错误信息

    # print(int('7.6'))

    print('END')
    s = '1'
    n = int(s)
    logging.info('n = %d' % n)
    print(10 / n)

    t = datetime(2022,10,21,23, 59, 59)
    print(t)

    t1 = t + timedelta(hours=-1,minutes=10)


    print(t1)

    print((t - t1).seconds)

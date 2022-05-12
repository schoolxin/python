# -*- coding:utf-8 -*-
# @FileName  :errorHandle.py
# @Time      :2022/5/11 18:28
# @Author    :dzz
# @Function  :
import logging
logging.basicConfig(level=logging.INFO)

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
    s = '0'
    n = int(s)
    logging.info('n = %d' % n)
    print(10 / n)

# -*- coding:utf-8 -*-
# @FileName  :Demo01.py
# @Time      :2022/6/16 17:48
# @Author    :dzz
# @Function  :


def num():
    n = 100
    print(n)
    a = yield 1
    while True:
        a = yield a


num()

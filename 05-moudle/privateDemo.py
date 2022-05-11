# -*- coding:utf-8 -*-
# @FileName  :privateDemo.py
# @Time      :2022/5/9 15:00
# @Author    :yhl
# @Function  :

import numpy


def _private_1(name):
    return 'Hello, %s' % name


def _private_2(name):
    return 'Hi, %s' % name


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)


if __name__ == "__main__":
    print(greeting("jacks"))
    print(_private_1("不应该引用private函数和变量"))

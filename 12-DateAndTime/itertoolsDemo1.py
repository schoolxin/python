# -*- coding:utf-8 -*-
# @FileName  :itertoolsDemo1.py
# @Time      :2022/6/9 10:47
# @Author    :dzz
# @Function  :
import itertools


def pi(N):
    natuals = itertools.count(1,2)

    ns = itertools.takewhile(lambda x: x <= 2*N - 1, natuals)

    l = list(ns)

    newl = list()

    count = 0
    sum = 0
    for item in l:
        print(item)
        count += 1
        if count % 2 == 0:
            newl.append(-4 / item)
        else:
            newl.append(4 / item)
    print(newl)
    for c in newl:
        sum += c
    print(sum)


if __name__ == "__main__":
    pi(10)

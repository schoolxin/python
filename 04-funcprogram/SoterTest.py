# -*- coding:utf-8 -*-
# @FileName  :SoterTest.py
# @Time      :2022/5/7 14:52
# @Author    :yhl
# @Function  :
from operator import itemgetter

if __name__ == "__main__":
    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    print(sorted(L, key=lambda x: x[1]))

    print(sorted(L, key=itemgetter(0)))



# -*- coding:utf-8 -*-
# @FileName  :TupleStudy.py
# @Time      :2022/4/20 17:02
# @Author    :yhl
# @Function  :
import math

if __name__ == "__main__":
    t1 = (1,)
    print(t1)
    hash_more = 1
    if hash_more:
        print("进入if")

    s = input('birth: ')
    birth = int(s)
    if birth < 2000:
        print('00前')
    else:
        print('00后')



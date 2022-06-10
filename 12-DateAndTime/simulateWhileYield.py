# -*- coding:utf-8 -*-
# @FileName  :simulateWhileYield.py
# @Time      :2022/6/9 15:11
# @Author    :dzz
# @Function  :

def get_orders():
    n = 2
    l1 = list(range(5))
    while n > 0:
        for i in l1:
            yield i
        n = n - 1


if __name__ == "__main__":

    for order in get_orders():
        print(order)

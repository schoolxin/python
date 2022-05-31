# -*- coding:utf-8 -*-
# @FileName  :ThreadDemo02.py
# @Time      :2022/5/30 18:06
# @Author    :dzz
# @Function  :

import threading, time

balance = 0
locks = threading.Lock()


def change_it2(n):
    print(balance)


def change_it(n):
    global balance
    balance = balance + n
    # print(balance)
    balance = balance - n


def thread_loop(n):
    locks.acquire()  # 获得锁
    for i in range(2200000):
        change_it(n)
    locks.release()  # 释放锁


if __name__ == "__main__":
    t1 = threading.Thread(target=thread_loop, args=(10,))
    t2 = threading.Thread(target=thread_loop, args=(20,))

    t1.start()

    t2.start()

    t1.join()

    t2.join()

    print(balance)
    # change_it2(100)
    # change_it(100)

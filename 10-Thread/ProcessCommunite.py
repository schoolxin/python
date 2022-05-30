# -*- coding:utf-8 -*-
# @FileName  :ProcessCommunite.py
# @Time      :2022/5/30 16:32
# @Author    :dzz
# @Function  :
import time
from multiprocessing import Queue
import os
from multiprocessing import Process


def read(q):
    print(f"Process to read {os.getpid()}")

    print(q)

    while True:
        # print("rttt")
        print(f"Get {q.get()} from queue")


def write(q):
    print(f"Process to write {os.getpid()}")

    for a in ['A', 'B', 'C']:
        print(f"Process write {a} to queue")

        q.put(a)

        time.sleep(2)


if __name__ == "__main__":
    q = Queue() # 进程间通过queue 进行通讯

    pw = Process(target=write, args=(q,))

    pr = Process(target=read,args=(q,))

    # 启动写进程
    pw.start()

    # 启动读进程
    pr.start()

    #等待写进程完成

    pw.join()

    #读继承是死循环 要强制终止

    pr.terminate()



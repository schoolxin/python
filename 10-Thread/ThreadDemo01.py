# -*- coding:utf-8 -*-
# @FileName  :ThreadDemo01.py
# @Time      :2022/5/30 17:29
# @Author    :dzz
# @Function  :
import time, threading


def funs():
    print(f"当前线程名为{threading.current_thread().name}")

    n = 0
    while n < 5:
        n = n + 1
        print(f"当前线程名为{threading.current_thread().name} n 为{n}")

if __name__ == "__main__":
    t = threading.Thread(target=funs, args=(), name="LoopThread")

    print(f"start当前线程名为{threading.current_thread().name}")
    t.start()
    t.join()

    print(f"end当前线程名为{threading.current_thread().name}")

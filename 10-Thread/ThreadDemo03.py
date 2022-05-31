# -*- coding:utf-8 -*-
# @FileName  :ThreadDemo03.py
# @Time      :2022/5/31 14:01
# @Author    :dzz
# @Function  :
import threading
import time

lock = threading.Lock()


class myThread(threading.Thread):

    def __init__(self, threadid, name, delay):
        threading.Thread.__init__(self)
        self.threadId = threadid
        self.threadName = name
        self.delay = delay

    def run(self):
        print(f"开始线程{self.threadName}")
        lock.acquire()  # 获得锁
        print_time(self.threadName, self.delay, 5)

        lock.release()  # 释放锁

        print("退出线程：" + self.name)


def print_time(threadName, delay, counter):
    # print("aaa"+threadName)
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


if __name__ == "__main__":
    thread1 = myThread(1, "Thread-1", 1)
    thread2 = myThread(2, "Thread-2", 2)

    thread1.start()
    thread2.start()

    thread1.join()

    thread2.join()

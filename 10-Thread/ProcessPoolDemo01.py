# -*- coding:utf-8 -*-
# @FileName  :ProcessPoolDemo01.py
# @Time      :2022/5/20 17:10
# @Author    :dzz
# @Function  :
import datetime
import os

from multiprocessing import Pool
import time
import subprocess


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()

    time.sleep(2)
    end = time.time()

    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == "__main__":
    run_code = 0
    print("Parent Process %s" % os.getpid())
    # print(datetime.datetime.now())
    # start = time.time()
    # print(start)
    # time.sleep(5)
    #
    # print(datetime.datetime.now())
    # end = time.time()
    # print(end)
    # print(end - start)

    # print(datetime.now())
    # print(time.time())

    p = Pool()  # Pool的默认大小为cpu的核数

    # 启动4个线程

    for i in range(1):
        p.apply_async(long_time_task, args=(i,))

    print('Waiting for all subprocesses done...')

    p.close()  # 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
    p.join()
    print("hhs")

    # print('All subprocesses done.')
    #
    # print('$ nslookup www.python.org')
    # r = subprocess.call(['nslookup', 'www.python.org'])
    # print('Exit code:', r)

    # print('$ nslookup')
    # p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    # print(output.decode("GBK"))
    # print('Exit code:', err)

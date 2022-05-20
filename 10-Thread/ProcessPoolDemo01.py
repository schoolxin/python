# -*- coding:utf-8 -*-
# @FileName  :ProcessPoolDemo01.py
# @Time      :2022/5/20 17:10
# @Author    :dzz
# @Function  :
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

    # print(datetime.now())
    # print(time.time())



    p = Pool(4)

    # 启动4个线程

    for i in range(4):
        p.apply_async(long_time_task, args=(i,))

    print('Waiting for all subprocesses done...')

    p.close()
    p.join()

    print('All subprocesses done.')
    #
    # print('$ nslookup www.python.org')
    # r = subprocess.call(['nslookup', 'www.python.org'])
    # print('Exit code:', r)

    print('$ nslookup')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    print(output.decode("GBK"))
    print('Exit code:', p.returncode)
1
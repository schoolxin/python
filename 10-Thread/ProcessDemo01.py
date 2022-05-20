# -*- coding:utf-8 -*-
# @FileName  :ProcessDemo01.py
# @Time      :2022/5/20 16:54
# @Author    :dzz
# @Function  :


from multiprocessing import Process
import os


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()  # 方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    print('Child process end.')

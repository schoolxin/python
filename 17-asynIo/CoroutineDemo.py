# -*- coding:utf-8 -*-
# @FileName  :CoroutineDemo.py
# @Time      :2022/6/16 17:44
# @Author    :dzz
# @Function  :

def consumer():
    r = ''
    while True:
        n = yield r

        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        t = c.send(n)
        print('[PRODUCER] Consumer return: %s' % t)
    c.close()


c = consumer()  # 返回一个生成器 函数不会被执行的
produce(c)

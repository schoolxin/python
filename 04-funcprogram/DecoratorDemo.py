# -*- coding:utf-8 -*-
# @FileName  :DecoratorDemo.py
# @Time      :2022/5/7 17:48
# @Author    :yhl
# @Function  :
import functools
import time


def log(func):
    @functools.wraps(func)  # 把原始函数的__name__等属性复制到wrapper()函数中
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        func(*args, **kw)

    return wrapper


# 把@log放到now()函数的定义处，相当于执行了语句：now = log(now)
@log
def now():
    print('2015-3-25')


print(now.__name__)


def metric(fn):
    @functools.wraps(fn)  # 把原始函数的__name__等属性复制到wrapper()函数中
    def wrapper(*args, **kw):
        print('call %s():' % fn.__name__)
        start = time.time()
        res = fn(*args, **kw)
        end = time.time()
        print('%s executed in %s ms' % (fn.__name__, end - start))
        return res;
    return wrapper
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

if __name__ == "__main__":
    print(fast(1,2))

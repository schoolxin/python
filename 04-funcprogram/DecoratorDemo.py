# -*- coding:utf-8 -*-
# @FileName  :DecoratorDemo.py
# @Time      :2022/5/7 17:48
# @Author    :yhl
# @Function  :
from datetime import datetime
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
        return res

    return wrapper


@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


if __name__ == "__main__":
    dt_now = datetime.fromtimestamp(time.time())
    print(dt_now)
    print(dt_now.strftime('%Y%m%d'))
    print(fast(1, 2))
    time_str = '2020-06-16 10:31:08'
    dt_time = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')  # 从字符串向datetime转化时，必须根据字符串的格式来订单strptime的第二个参数format
    print(dt_time)
    time_str1 = '2020/10/17'
    dt_time1 = datetime.strptime(time_str1, '%Y/%m/%d')
    print(dt_time1)  # 2020-06-17 00:00:00

    print(dt_time1.strftime("%Y/%#m/%d"))  # 字符串转为日期型 月份如果是单月份 前面不会有0

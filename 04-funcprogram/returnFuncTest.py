# -*- coding:utf-8 -*-
# @FileName  :returnFuncTest.py
# @Time      :2022/5/7 16:11
# @Author    :yhl
# @Function  :
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


if __name__ == "__main__":
    num = [1, 2, 3, 3]
    f1 = lazy_sum(*num)
    print(f1())


    def inc():
        x = 0

        def fn():
            nonlocal x  # 所以需要在fn()函数内部加一个nonlocal x的声明。加上这个声明后，解释器把fn()的x看作外层函数的局部变量
            x = x + 1
            return x

        return fn


    f = inc()
    print(f())  # 1
    print(f())  # 2

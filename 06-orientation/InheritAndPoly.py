# -*- coding:utf-8 -*-
# @FileName  :InheritAndPoly.py
# @Time      :2022/5/9 16:16
# @Author    :yhl
# @Function  :
'''
继承和多态
'''


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


class duck():
    def power(self):
        return 100


class duck2():
    def power(self):
        return 100


def run_twice(duck):
    print(duck.power())


if __name__ == "__main__":
    obj = MyObject()
    print(getattr(obj, 'x'))  # 获取属性的值
    print(hasattr(obj, 'y'))  # 判断对象中是否有该属性
    if hasattr(obj, 'y'):
        print(getattr(obj, 'y'))
    else:
        setattr(obj, 'y', 100)  # 设置属性的值

    print(getattr(obj, 'y'))

    print("也可以获取到对象中的方法")

    fn1 = getattr(obj, 'power')

    print(fn1())

    d2 = duck2()

    run_twice(d2)

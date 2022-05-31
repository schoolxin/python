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


class Errors(object):

    def __init__(self, mess):
        print("222")
        self._mess = mess

    def __str__(self):
        return self._mess


class Errors_c(Errors):
    print("ss")
    pass


class p1():
    def __init__(self, group=None, target=None):
        print("diudiu")
        # self.name = name
    def show(self):
        print("woshifuqin")


class c1(p1):
    def __init__(self, height, age):
        self.height = height
        self.age = age


if __name__ == "__main__":
    c1 = c1("zhangsna", 100)
    print(c1.height)
    c1.show()
# e = Errors_c("hhh")
# print(e._mess)

# obj = MyObject()
# print(getattr(obj, 'x'))  # 获取属性的值
# print(hasattr(obj, 'y'))  # 判断对象中是否有该属性
# if hasattr(obj, 'y'):
#     print(getattr(obj, 'y'))
# else:
#     setattr(obj, 'y', 100)  # 设置属性的值
#
# print(getattr(obj, 'y'))
#
# print("也可以获取到对象中的方法")
#
# fn1 = getattr(obj, 'power')
#
# print(fn1())
#
# d2 = duck2()
#
# run_twice(d2)

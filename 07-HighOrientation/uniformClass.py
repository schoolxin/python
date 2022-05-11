# -*- coding:utf-8 -*-
# @FileName  :uniformClass.py
# @Time      :2022/5/11 11:39
# @Author    :dzz
# @Function  :
class Fib(object):
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        # self.a = self.b
        # self.b = self.a + self.b
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值


class Fib1:
    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):
            start = item.start
            end = item.stop
            a, b = 1, 1
            l1 = []
            for n in range(end):
                if n >= start:
                    l1.append(a)
                a, b = b, a + b
            return l1


class Student(object):

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def __getattr__(self, attr):  # 该方法只有在没有找到属性的情况下 进行调用
        if attr == 'age':
            print("hhh")
            return lambda: 25  # 这个匿名函数 lambda 没有参数
    def __call__(self, *args, **kwargs): # 在实例本身调用时 调用该方法 s = Student() s()
        print('My name is %s.' % self.name)


if __name__ == "__main__":
    print("如果一个类想被for in  循环，就必须实现一个__iter__()方法，该方法返回一个迭代对象 然后，Python的for循环就会不断调用该迭代对象的__next__()方法")

    for n in Fib():
        print(n)
    print("要表现得像list那样按照下标取出元素，需要实现__getitem__()方法")

    f = Fib1()

    print(f[0])

    print(f[5])
    print(f[1:3])

    s = Student()
    print(s.age())
    s.name = 100

    print(s.name)

    s()

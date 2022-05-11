# -*- coding:utf-8 -*-
# @FileName  :slotsDemo.py
# @Time      :2022/5/9 18:50
# @Author    :yhl
# @Function  :
from types import MethodType


class Student(object):
    __slots__ = ("age", "name", "set_age")
    pass


def set_age(self, age):
    self.age = age


if __name__ == "__main__":
    s1 = Student()
    s1.name = "lisi"
    s1.set_age = MethodType(set_age, s1)  # 给实例绑定方法 set_age 可以当做是 实例的一个属性
    s1.set_age(100)
    print(s1.age)
    s2 = Student()

    # s2.setAge(100) # 给s1绑定的方法 setAge在其他实例中是无效的  如果想给所有的实例都绑定一个方法 可以给class 绑定

    # 因为`MethodType(f, x)`的第二个参数x，实际就是以后执行 f 时代入的self。
    # Student.setAge1 = MethodType(set_age, s1)
    # s3 = Student()
    # s3.setAge1("s3")
    #
    # print(s3.age)

    print("使用__slots__ 来限定类的实例中只能添加某个属性")

    print("使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的")

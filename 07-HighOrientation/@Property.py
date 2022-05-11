# -*- coding:utf-8 -*-
# @FileName  :@Property.py
# @Time      :2022/5/10 9:30
# @Author    :dzz
# @Function  :
class Student(object):

    def __init__(self):
        self._age = 0
        self._birth = '1997-01-01'

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return self._age


class Screen(object):

    def __len__(self):
        return 9999

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._height * self._width


if __name__ == "__main__":
    print("@property作用就是将方法变成属性一样来使用")
    s1 = Student()
    s1.birth = '2022-05-10'
    print(s1.birth)

    # print(s1._age)

    sc1 = Screen()

    sc1.height = 100
    sc1.width = 100
    print(sc1.resolution)
    print(len(sc1))

# -*- coding:utf-8 -*-
# @FileName  :ClassAndInstance.py
# @Time      :2022/5/9 15:44
# @Author    :yhl
# @Function  :


'''
    ws
'''


class Student(object):

    def __init__(self, name, age, score=90):  # 相当于java中的构造方法
        self.__name = name  # 两个下划线__ 表示将变量变成了一个私有变量  私有变量不能在类外部访问了
        self.__age = age
        self.__score = score

    def print_score(self):
        print(f"name={self.__name}==>age={self.__age}")

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_name(self):
        return self.__name


if __name__ == "__main__":
    s1 = Student('Lisa', 99)
    s1.addr = 'beijing'
    s1.print_score()
    s1.__name = "mask"
    print(s1.get_name())

# -*- coding:utf-8 -*-
# @FileName  :enumDemo.py
# @Time      :2022/5/11 16:11
# @Author    :dzz
# @Function  :
from enum import Enum, unique


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


class Gender(Enum):
    Male = 0

    Female = 1


class Student(object):

    def __init__(self, name, gender):
        self.name = name

        self.gender = Gender(gender)


if __name__ == "__main__":

    Months = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov',
                            'Dec'))  # Month相当于一个class类型，然后，每个常量都是class的一个唯一实例

    print(Months.Jan)  # 访问枚举中的值
    print(Months.Jan.name)  # 访问枚举中的值的name属性
    print(Months.Jan.value)  # 访问枚举中的值的value属性

    for name, member in Months.__members__.items():
        print(name, "=>", member, member.value)

    print("我是分割线==============")
    print("1." + Weekday['Sat'].name)
    print("2." + Weekday.Sat.name)
    print("3." + Weekday(1).name)

    print("weekday")
    for name, member in Weekday.__members__.items():
        print(name, "=>", member, "=>", member.value)

    print("Student")
    bart = Student('Bart', 0)
    # print()

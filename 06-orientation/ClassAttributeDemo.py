# -*- coding:utf-8 -*-
# @FileName  :ClassAttributeDemo.py
# @Time      :2022/5/9 18:19
# @Author    :yhl
# @Function  :
class Student1():
    name = 'Student'

    count = 0

    def __init__(self):
        self.age = 100

        Student1.count += 1  # 每创建一个Student1的实例 count就会加一


if __name__ == "__main__":
    print(Student1.count)
    s1 = Student1()

    print(Student1.count)
    # s1.name = "newStudent"  # 相当于给自己的对象条件了一个name的属性 会覆盖类中相同名字的属性
    # print(s1.name)
    # print(Student1.name)
    s2 = Student1()
    print(Student1.count)
    # print(s2.name)  # s2 没有name属性 则会查找class中的name属性

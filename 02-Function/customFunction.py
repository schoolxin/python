# -*- coding:utf-8 -*-
# @FileName  :customFunction.py
# @Time      :2022/4/29 16:04
# @Author    :yhl
# @Function  :
import math


def myabs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x > 0:
        return x
    else:
        return -x


# 函数可以返回多个值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


print("默认参数")


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print("默认参数应该使用不可变对象否则可能会出现问题")


def add_end(L=[]):
    L.append('END')
    return L


print("可变参数")


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + math.pow(n, 2)
    return sum


print("关键参数")


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
    print(type(kw))


print("命名关键字参数")


def person2(name, age, *, city, job):
    print(name, age, city, job)


def person3(name, age, *args, city, job):
    print(name, age, args, city, job)

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)




if __name__ == "__main__":
    # print(myabs(10))
    # print(myabs(-100))
    # print(myabs("A"))

    x, y = move(10, 20, 1)
    print(f"x={x} y={y}")
    print(x, y)
    print(move(10, 20, 1))

    print(power(3, 3))
    print("默认参数异常情况")
    print(add_end())
    print(add_end())

    print("可变参数 这些可变参数在函数调用时自动组装为一个tuple")
    print(calc(2, 3, 4))
    num = [2, 3, 4]
    print(calc(*num))  # 将一个已经定义好的列表或者元组 作为可变参数是 需要前面加一个* 表示将列表或元组变成可变参数传递

    print("而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict")
    person("Bobo", 100, city="beijing", gender="男")
    extra = {'city': 'Beijing', 'job': 'Engineer'}
    person("Bobo", 100, **extra)  # 将一个已经定义好的dict 作为可变参数是 需要前面加一个** 表示dict中的参数作为关键字参数传入

    print("命名关键字参数 主要是为了限制参数的名字必须和函数订单的参数列表中的名字一样")
    print("命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数")
    person2('Jack', 24, city='Beijing', job='Engineer')
    # person2('Jack', 24, 'Beijing', 'Engineer') #如果没有传入参数名，调用将报错：

    print("如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：")
    # person3('Jack', 24, 'Beijing', 'Engineer') #如果没有传入参数名，调用将报错：
    person3('Jack', 24,  city="beijing", job="Engineer")
    print("参数组合：参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数")

    args = (1, 2, 3, 4)
    f1(*args)

    move(4, 'A', 'B', 'C')




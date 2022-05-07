# -*- coding:utf-8 -*-
# @FileName  :MapAndReduce.py
# @Time      :2022/5/6 18:01
# @Author    :yhl
# @Function  :
from functools import reduce

if __name__ == "__main__":
    list1 = [2, 12, 32, 12, 12]

    print("将数字变成字符串")
    newList = map(str, list1)  # 由于结果newList是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
    print(list(newList))

    print("reduce  归约函数")
    # [1, 3, 5, 7, 9]变换成整数13579

    list2 = [1, 3, 5, 7, 9]


    def fn(x, y):
        return x * 10 + y


    print(reduce(fn, list2))

    print("把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字")

    L1 = ['adam', 'LISA', 'barT']
    # print('add'.capitalize())
    newL1 = map(lambda x: x.capitalize(), L1)
    print(list(newL1))

    print("请编写一个prod()函数，可以接受一个list并利用reduce()求积")


    def prod(L):
        return reduce(lambda x, y: x * y, L)


    print(prod([3, 5, 7, 9]))

    print("将浮点型的字符串转成浮点数")

    s = "123.456";

    CHAR_TO_FLOAT = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '.': -1
    }


    def str2float(s1):
        # print(s1)
        nums = map(lambda x: CHAR_TO_FLOAT.get(x), s1)
        nums2 = map(lambda x: CHAR_TO_FLOAT.get(x), s1)
        print(list(nums2))
        point = 0

        def toFloats(result, data):
            print("data" + str(data))
            nonlocal point  # 自由变量是指未绑定到本地作用域的变量。如果自由变量绑定的值是可变的，变量仍然可以在封闭包中操作。如果是不可变的(数字、字符串等。)，在封闭包中重新绑定自由变量会出错。
            if data == -1:
                point = 1
                return result
            if point == 0:
                result = result * 10 + data
                return result
            else:
                point = point * 10
                result = result + data * 1.0 / point
                return result

        return reduce(toFloats, nums, 0)  # reduce 的第三个参数表示的初始值


    print(str2float('.456'))

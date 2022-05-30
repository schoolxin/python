# -*- coding:utf-8 -*-
# @FileName  :custom_trim.py
# @Time      :2022/5/5 16:01
# @Author    :yhl
# @Function  :
from collections.abc import Iterable
import os


def mytrim(s):
    newStr = ""
    print(s[0:1])
    print(s[-1:])
    if (s[0:1] == " " and s[-1:] == " "):
        newStr = s[1:][:-1]
    elif s[0:1] == " ":
        newStr = s[1:]
    elif s[-1:] == " ":
        newStr = s[:-1]
        print(newStr)
    else:
        newStr = s[:]

    return newStr


def findMinAndMax(L1):
    max = 0
    min = 0
    for l in L1:
        if l >= max:
            max = l
        if l <= min:
            min = l
    return (max, min)


if __name__ == "__main__":
    # if mytrim('hello  ') != 'hello':
    #     print('测试成功1!')
    # elif mytrim('  hello') != 'hello':
    #     print('测试成功2!')
    # elif mytrim('  hello  ') != 'hello':
    #     print('测试成功3!')
    # elif mytrim('  hello  world  ') != 'hello  world':
    #     print('测试成功4!')
    # elif mytrim('') != '':
    #     print('测试成功5!')
    # elif mytrim('    ') != '':
    #     print('测试成功6!')
    # else:
    #     print('测试成功!')
    #
    # print("迭代测试")
    #
    # dict1 = {"name": "zhansan", "age": 100, "sex": "男"}
    #
    # for key, value in dict1.items():
    #     print(key, value)
    #
    # print(isinstance('abc', Iterable))
    # print(isinstance((1, 2, 3), Iterable))
    # print(isinstance(123, Iterable))
    #
    # print("enumerate 可以将一个list变成一个索引-元素数 这样就可以同时迭代索引和元素")
    #
    # list1 = [2, 3, 34, 443, 23]
    # for index, value in enumerate(list1):
    #     print(index, value, list1[index])
    #
    # for x, y in [(1, 1), (2, 4), (3, 9)]:
    #     print(x, y)
    #
    # print("利用迭代获取列表中最大和最小值")
    # print(findMinAndMax([7]))
    # print(findMinAndMax([1, 2, 4, 8, 19, 3, 5]))
    #
    # print("列表生成式")
    #
    # list3 = [x * x for x in range(1, 11)]
    # print(list3)
    #
    # list4 = [x * -x for x in range(1, 10) if x % 2 == 0]  # 最后的if是个筛选条件 不能带else
    # print("list4" + str(list4))
    # print("生成一个全排列")
    #
    # list5 = [m + n for m in 'abc' for n in 'xyz']
    # print(list5)
    # print("使用列表生成式 列出目录下所有的文件和目录名")
    #
    # list6 = [d for d in os.listdir("..")]
    #
    # print(list6)
    #
    # list7 = [x * x if x % 2 == 0 else -x for x in
    #          range(1, 10)]  # 如果把if 写到for 前面必须要加上else 因为for前面是个表达式 必须要算出来一个值才可以 考察表达式：x if x % 2 == 0
    # print("list7" + str(list7))
    #
    # L1 = ['Hello', 'World', 18, 'Apple', None]
    # L2 = [l.lower() for l in L1 if isinstance(l, str)]
    #
    # print(L2)
    # if L2 == ['hello', 'world', 'apple']:
    #     print('测试通过!')
    # else:
    #     print('测试失败!')
    # # print(isinstance(None,str))
    #
    # print("生成器")
    #
    # lt1 = (g for g in range(1, 11))
    # for n in lt1:
    #     print(n)
    #
    # print("fib")
    #
    #
    # def fib(max):
    #     n, a, b = 0, 0, 1
    #     while n < max:
    #         yield b
    #         a, b = b, a + b
    #         n = n + 1
    #
    #
    # f = fib(6)
    # for i in fib(10):
    #     print(i)
    #
    #
    # def func(a):
    #     def func_1(n):
    #         if n == 0:
    #             print("tt" + str(tt))
    #             return 0
    #
    #         elif n == 1 or n == 2:
    #             return 1
    #         else:
    #             return func_1(n - 2) + func_1(n - 1)
    #     tt = 100
    #
    #     list_1 = []
    #     for i in range(a):
    #         list_1.append(func_1(i))
    #     return list_1
    #
    #
    # print(func(20))

    print("杨辉三角")


    def triangles():
        print("whh")
        ret = [1]
        while True:
            yield ret  # 遇到yield 就中断 下次调用时从上次中断处往下继续运行
            for i in range(1, len(ret)):
                # print("v"+str(v))
                ret[i] = pre[i] + pre[i - 1]
            v = 100
            ret.append(1)
            pre = ret[:]


    def searchorder():
        print("waaa")
        i = 0
        while True:
            i = i + 1
            for j in range(3):
                yield j
            if i > 3:
                break


    for i in searchorder():
        print(i)

    n = 0
    results = []
    # triangles()

    # for t in triangles():
    #     print(t)
    #     results.append(t)
    #     n = n + 1
    #     if n == 10:
    #         break

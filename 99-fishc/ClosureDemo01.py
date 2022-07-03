# -*- coding:UTF-8 -*-
# file_name     :ClosureDemo01.py
# create_date   :2022/7/3 
# author         : dzz
'闭包'


def funcOut(x):
    def funcIn(y):
        return x * y

    return funcIn


fc = funcOut(10)

print(fc)
print(fc(50))


def f1():
    x = 5
    def f2():
        nonlocal x
        x = x + 1
        return x
    return f2()

print("nonlocal")
print(f1())

if __name__ == '__main__':
    pass

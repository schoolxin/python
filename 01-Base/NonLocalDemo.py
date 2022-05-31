# -*- coding:utf-8 -*-
# @FileName  :NonLocalDemo.py
# @Time      :2022/5/30 18:29
# @Author    :dzz
# @Function  :
a = 15


def fun1():
    global b

    b = 100
    a = 4

    def fun2():
        nonlocal a  # nonlocal 方法只修改离它最近的一层函数的变量，如果这一层没有就往上一层查找，只能在局部查找
        a = a + 1
        print(f"func2 a = {a}")

    fun2()
    print(f"func1 a = {a}")


if __name__ == "__main__":
    a = 10


    def func():
        a = 5

        def foo():
            a = 3

            def f():
                nonlocal a
                a = a + 1

                def aa():
                    a = 1

                    def b():
                        global a
                        a = a + 1
                        print(a)

                    b()
                    print(a)

                aa()
                print(a)

            f()
            print(a)

        foo()
        print(a)


    func()
    print(a)

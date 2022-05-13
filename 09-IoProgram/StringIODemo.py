# -*- coding:utf-8 -*-
# @FileName  :StringIODemo.py
# @Time      :2022/5/12 17:34
# @Author    :dzz
# @Function  :

from io import StringIO

if __name__ == "__main__":

    f = StringIO()
    f.write("hello")
    f.write("world")
    print(f.getvalue())
    print('中文'.encode('utf-8'))

    while True:
        s = f.readline()
        # print("hh"+s.strip())
        if s == "":
            break
    f1 = StringIO("abc")
    print(f1.getvalue())
    f1.write("def") # 这个时候指针还在0的位置 这个时候写 将从0的位置开始写 也就覆盖了之前的数据
    print("指针位置"+f1.tell())
    while True:
        s = f1.readline()
        print("hh"+s.strip())
        if s == "":
            break
    print(f1.getvalue())


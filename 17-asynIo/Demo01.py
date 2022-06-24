# -*- coding:utf-8 -*-
# @FileName  :Demo01.py
# @Time      :2022/6/16 17:48
# @Author    :dzz
# @Function  :

def test(val=1):
    while True:
        y = yield val
        val = y
        print(f"y:{y}")


t = test()

print(next(t))
print(t.send("hello"))

# -*- coding:utf-8 -*-
# @FileName  :turtleDemo01.py
# @Time      :2022/6/14 15:33
# @Author    :dzz
# @Function  :

from turtle import *

if __name__ == "__main__":
    # 设置笔刷宽度:
    width(4)

    # 前进:
    forward(400)
    # 右转90度:
    right(90)

    # 笔刷颜色:
    pencolor('red')
    forward(100)
    right(90)

    pencolor('green')
    forward(200)
    right(90)

    pencolor('blue')
    forward(100)
    right(90)

    # 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
    done()

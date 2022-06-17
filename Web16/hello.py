# -*- coding:utf-8 -*-
# @FileName  :hello.py
# @Time      :2022/6/16 11:34
# @Author    :dzz
# @Function  :

# application 函数：
# environ：一个包含所有HTTP请求信息的dict对象；

# start_response：一个发送HTTP响应的函数。
i= 0

def applications(environ, start_response2):
    global i
    i = i + 1
    print(i)
    start_response2('200 OK', [('Content-Type', 'text/html')])  # 发送头
    return [b'<h1>Hello, web!</h1>']  # 响应的数据 发送给浏览器

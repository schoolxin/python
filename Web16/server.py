# -*- coding:utf-8 -*-
# @FileName  :server.py
# @Time      :2022/6/16 11:38
# @Author    :dzz
# @Function  :

# 从wsgiref模块导入:
from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数:
from Web16.hello import applications

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('localhost', 7777, applications)
print('Serving HTTP on port 7777...')
# 开始监听HTTP请求:
httpd.serve_forever()

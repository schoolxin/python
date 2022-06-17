# -*- coding:utf-8 -*-
# @FileName  :asyncioDemo1.py
# @Time      :2022/6/17 10:07
# @Author    :dzz
# @Function  :


import asyncio


@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(2)
    print(r)
    print("Hello again!")


# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()

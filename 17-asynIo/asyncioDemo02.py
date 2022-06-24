# -*- coding:utf-8 -*-
# @FileName  :asyncioDemo02.py
# @Time      :2022/6/17 10:15
# @Author    :dzz
# @Function  :


import asyncio


@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)

    port = 80 if host == "www.sohu.com" else 90
    connect = asyncio.open_connection(host, port)
    reader, writer = yield from connect
    # print("ttt")
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    print('%s ok' % host)
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()


loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

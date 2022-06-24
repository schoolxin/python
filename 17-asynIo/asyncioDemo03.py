# 使用同步方式编写异步功能
import time
import asyncio


@asyncio.coroutine  # 标志协程的装饰器
def taskIO_1():
    print('开始运行IO任务1...')
    yield from asyncio.sleep(1)  # 假设该任务耗时2s
    print('IO任务1已完成，耗时1s')
    return taskIO_1.__name__


@asyncio.coroutine  # 标志协程的装饰器
def taskIO_2():
    print('开始运行IO任务2...')
    yield from asyncio.sleep(10)  # 假设该任务耗时3s
    print('IO任务2已完成，耗时10s')
    return taskIO_2.__name__


@asyncio.coroutine  # 标志协程的装饰器
def main():  # 调用方
    tasks = [taskIO_2(), taskIO_1()]  # 把所有任务添加到task中
    done, pending = yield from asyncio.wait(tasks)  # 子生成器 同时通过yield from返回一个包含(done, pending)的元组
    for r in done:  # done和pending都是一个任务，所以返回结果需要逐个调用result()
        print('done协程无序返回值：' + r.result())
    for r in pending:  # done和pending都是一个任务，所以返回结果需要逐个调用result()
        print('pending协程无序返回值：' + r.result())



if __name__ == '__main__':
    start = time.time()
    loop = asyncio.get_event_loop()  # 创建一个事件循环对象loop
    try:
        loop.run_until_complete(main())  # 完成事件循环，直到最后一个任务结束
    finally:
        loop.close()  # 结束事件循环
    print('所有IO任务总耗时%.5f秒' % float(time.time() - start))

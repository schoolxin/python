# -*- coding:utf-8 -*-
# @FileName  :ChainTest.py
# @Time      :2022/5/11 15:19
# @Author    :dzz
# @Function  : Chain().users('michael').repos输出/users/michael/repos

class Chain(object):
    count = 1

    def __init__(self, path=''):
        print(Chain.count)
        Chain.count += 1
        self._path = path

    def __getattr__(self, path):
        print("1" + path)
        return Chain('%s/%s' % (self._path, path))

    def __call__(self, path):  # 实例本身调用时 该方法会被执行
        print("2" + path)
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        print("3" + self._path)
        return self._path


if __name__ == "__main__":
    Chain().users('michael').repos

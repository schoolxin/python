# -*- coding:utf-8 -*-
# @FileName  :OrderedDictDemo.py
# @Time      :2022/6/8 16:39
# @Author    :dzz
# @Function  :

from collections import OrderedDict


class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        print(self)
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


if __name__ == "__main__":
    od1 = LastUpdatedOrderedDict(2)

    od1["name"] = "zhangsan"

    od1["age"] = 100

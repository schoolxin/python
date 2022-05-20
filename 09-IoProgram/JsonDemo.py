# -*- coding:utf-8 -*-
# @FileName  :JsonDemo.py
# @Time      :2022/5/20 13:53
# @Author    :dzz
# @Function  :
import json
import pickle


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


if __name__ == "__main__":
    print("json测试")
    json_str = '{"age": 20, "score": 88, "name": "Bob"}'

    dict1 = json.loads(json_str)

    print(dict1)
    s = Student('Bob', 20, 88)

    print(json.dumps(s, default=lambda obj: obj.__dict__))  # dump()方法可以直接把JSON写入一个file-like Object

    d = dict(name='Bob', age=20, score=88)

    f = open("dump.txt", "wb")
    f.write(pickle.dumps(d))
    f.close()

    # print(pickle.dumps(d)) #pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
    f = open('dump.txt', 'rb')
    d = pickle.load(f)
    f.close()

    f1 = open("dump1.txt", "w")
    json.dump(d, f1)  # 将python类json对象这些写入到文件

    f1.close()

    # 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：

    with open("dump1.txt", "r") as f2:
        print("json 反序列化")
        print(json.load(f2))

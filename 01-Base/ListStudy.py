# -*- coding:utf-8 -*-
# @FileName  :ListStudy.py
# @Time      :2022/4/20 15:38
# @Author    :yhl
# @Function  :


if __name__ == "__main__":
    classmates = ['Michael', 'Bob', 'Tracy']
    print(f"列表长度${len(classmates)}")

    print("访问列表中的元素")

    for idx, elem in enumerate(classmates):
        print(idx, elem)
    print("列表是一个可变的有序表 可以往里面追加数据")

    classmates.append("Adam")
    for idx, elem in enumerate(classmates):
        print(idx, elem)

    print("删除元素")

    # popelem = classmates.pop()  # 删除最后一个元素并将删除的元素进行返回
    # print(popelem)
    for idx, elem in enumerate(classmates):
        print(idx, elem)
    # popelem1 = classmates.pop(1)  # 删除指定下标的元素并将删除的元素返回
    # print(popelem1)
    # for idx, elem in enumerate(classmates):
    #     print(idx, elem)

    print("修改指定位置上的元素")

    classmates[1] = 'Sara'
    for idx, elem in enumerate(classmates):
        print(idx, elem)



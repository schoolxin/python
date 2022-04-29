# -*- coding:utf-8 -*-
# @FileName  :mapStudy.py
# @Time      :2022/4/20 17:50
# @Author    :yhl
# @Function  :


if __name__ == "__main__":
    d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
    # d['Thomas'] # 这种访问可能会报错 所以推荐使用get方法取值 如果要用这种形式，可以先判断key是否存在 'Thomas' in d
    if d.get('Thomas') is None:  # 取不到就会返回None
        print("没有取到key对应的值")
    pop1 = d.pop('Bob')  # 删除对应的key  value值也会被删除 同时返回key对应的值

    print(pop1)
    print(d)

    t1 = [1, 2, 3]
    s1 = set(t1)
    print(t1)
    s1.add(100)
    print(s1)
    print(t1)

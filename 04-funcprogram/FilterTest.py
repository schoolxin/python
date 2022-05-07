# -*- coding:utf-8 -*-
# @FileName  :FilterTest.py
# @Time      :2022/5/7 13:52
# @Author    :yhl
# @Function  :


if __name__ == "__main__":
    str1 = 'abc'
    print(str1[::-1])


    def is_palindrome(n):
        nstr = str(n)
        print(nstr[::-1])
        print(nstr[::-1])
        if nstr == nstr[::-1]:
            return True
        else:
            return False

    filterL = filter(is_palindrome, [1, 2, 3, 45, 55, 99])

    # 注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
    print(list(filterL))

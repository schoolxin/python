# -*- coding:utf-8 -*-
# @FileName  :regexDemo01.py
# @Time      :2022/6/2 16:17
# @Author    :dzz
# @Function  :
import re

if __name__ == "__main__":
    test = '用户输入的字符串'
    if re.match(r'正则表达式', test):
        print('ok')
    else:
        print('failed')

    m = re.match(r'^(\d{3})-(\d{3,8})', '010-223-aa')
    print(m.group(0))

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

    m = re.match(r'^(\d{3})-(\d{3,8})', '010-22355-aa')
    print(m.group(0))
    re1 = re.compile(r'UTC([\-\+])(\d{1,2})')
    tz_str = 'UTC-09:00'
    print(re1.match(tz_str)[1])
    print(re1.match(tz_str)[2])


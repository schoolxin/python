# -*- coding:utf-8 -*-
# @FileName  :base64Demo1.py
# @Time      :2022/6/8 17:28
# @Author    :dzz
# @Function  :
import base64


def safe_base64_decode(s):
    while (len(s) % 4 != 0):
        s = s + '='

    s = base64.b64decode(s)

    print(s)


if __name__ == "__main__":
    safe_base64_decode('MTIzNDU2')

# -*- coding:utf-8 -*-
# @FileName  :urllibDemo1.py
# @Time      :2022/6/9 15:17
# @Author    :dzz
# @Function  :
import json
from urllib import request



def fetch_data(url):
    with request.urlopen(url) as f:
        data = f.read()

        data.decode('utf-8')
        print(data)
        datas = data.decode('utf-8')
        print(datas)
        print(type(json.loads(datas)))




if __name__ == "__main__":
    fetch_data("http://www.httpbin.org/get")

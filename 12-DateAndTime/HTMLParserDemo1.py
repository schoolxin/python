# -*- coding:utf-8 -*-
# @FileName  :HTMLParserDemo1.py
# @Time      :2022/6/9 18:12
# @Author    :dzz
# @Function  :
import re
from html.parser import HTMLParser
from urllib import request


class MyHTMLParser(HTMLParser):

    def __init__(self):
        super(MyHTMLParser, self).__init__()
        self.__flag = ''  # 用来存储标签的信息  方便提取数据是做判断
        self.result = []  # 将数据存储在列表中

    def handle_starttag(self, tag, attrs):
        if ('class', 'event-title') in attrs:
            self.__flag = "name"
        if tag == "time":
            self.__flag = "time"
        if ('class', 'say-no-more') in attrs:
            self.__flag = "year"
        if ('class', 'event-location') in attrs:
            self.__flag = "location"

    def handle_endtag(self, tag):
        self.__flag = ''  # 在HTML 标签结束时，把标志位清空

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_data(self, data):

        if self.__flag == "name":
            # dicts["会议名称"] = data
            self.result.append(f"会议名称：{data}")
        if self.__flag == "time":
            # dicts["时间"] = data
            self.result.append(f"时间：{data}")
        if self.__flag == "year":
            if re.match(r'\s\d{4}', data):
                # dicts["年"] = data
                self.result.append(f"年：{data}")
        if self.__flag == "location":
            self.result.append(f"地点：{data}")

    def handle_comment(self, data):
        pass

    def handle_entityref(self, name):
        pass

    def handle_charref(self, name):
        pass


if __name__ == "__main__":
    parser = MyHTMLParser()
    url = "https://www.python.org/events/python-events/"
    with request.urlopen(url) as f:
        datas = f.read()
        # print(datas)
        parser.feed(datas.decode('utf-8'))  # feed 的时候 就开始调用相关的 标签或元素的处理函数

    print(parser.result)

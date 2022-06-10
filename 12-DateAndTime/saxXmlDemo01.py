# -*- coding:utf-8 -*-
# @FileName  :saxXmlDemo01.py
# @Time      :2022/6/9 16:37
# @Author    :dzz
# @Function  :
from xml.parsers.expat import ParserCreate


class DefaultSaxHandler(object):

    def __init__(self):
        self.data = {}
        self.name = ''

    def start_element(self, name, attrs):
        self.name = name
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        self.data[self.name] = text
        print('sax:char_data: %s' % text)


if __name__ == "__main__":
    xml = r'''<?xml version="1.0"?>
    <ol>
        <li><a href="/python">Python</a></li>
        <li><a href="/ruby">Ruby</a></li>
    </ol>
    '''

    handler = DefaultSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml)

    print("+++++++++++++++")
    print(handler.data)

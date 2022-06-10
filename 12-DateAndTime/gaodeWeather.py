# -*- coding: utf-8 -*-
# @author xian_wen
# @date 5/14/2021 5:47 PM

from urllib import request
from xml.parsers.expat import ParserCreate


class DefaultSaxHandler(object):
    def __init__(self):
        self.data = {}
        self.name = ''

    def start_element(self, name, attrs):
        self.name = name
        # print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        pass

    def char_data(self, text):
        self.data[self.name] = text
        # print('sax:char_data: %s' % text)


def get_weather_info(url, city, key):
    real_url = url.format(city, key)

    print(real_url)
    with request.urlopen(real_url, timeout=4) as f:
        datas = f.read()
        return datas.decode('utf-8')


def parse_Xml(xml):
    handler = DefaultSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml)

    print(handler.data)

if __name__ == "__main__":
    url = "https://restapi.amap.com/v3/weather/weatherInfo?city=110000&key=000ef91caf1308f9972fc1a6bb63cd6a&output=xml"
    xml = get_weather_info(url, 110000, '000ef91caf1308f9972fc1a6bb63cd6a')

    parse_Xml(xml)

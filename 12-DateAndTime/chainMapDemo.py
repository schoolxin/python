# -*- coding:utf-8 -*-
# @FileName  :chainMapDemo.py
# @Time      :2022/6/8 15:37
# @Author    :dzz
# @Function  :
from collections import ChainMap
import os, argparse

if __name__ == "__main__":
    # 构造缺省参数:
    defaults = {
        'color': 'red',
        'user': 'guest'
    }

    # 构造命令行参数:
    parser = argparse.ArgumentParser()
    parser.add_argument('-u2', '--user')
    parser.add_argument('-c2', '--color')
    namespace = parser.parse_args()
    print(vars(namespace))
    command_line_args = {k: v for k, v in vars(namespace).items() if v}

    print(command_line_args)

    # 组合成ChainMap:
    combined = ChainMap(command_line_args, os.environ, defaults)

    # 打印参数:
    print('color=%s' % combined['color'])
    print('user=%s' % combined['user'])

# -*- coding:utf-8 -*-
# @FileName  :findFile.py
# @Time      :2022/5/13 17:06
# @Author    :dzz
# @Function  :在指定的路径中 查找文件名包含指定字符串的文件
import os


def findFiles(path, targetfile):
    # 获取指定目录下所有的文件和目录 然后遍历 所有文件，如果是目录 递归调用findFiles 再查找文件夹下的文件或文件夹
    files = [x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))]
    dirs = [x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))]

    for f in files:
        if targetfile in f:
            print(os.path.join(path, f))

    for d in dirs:
        findFiles(os.path.join(path, d),targetfile)


if __name__ == "__main__":

    findFiles("E:\export","export_data")

# -*- coding:utf-8 -*-
# @FileName  :HandleFileAndDir.py
# @Time      :2022/5/12 18:15
# @Author    :dzz
# @Function  :
import os

if __name__ == "__main__":
    # s = os.path.abspath('.')  # 当前目录的绝对路径

    f = os.path.join('F:/study/python/study', 'testdir')

    # os.mkdir(f)
    # os.rmdir(f)

    print(os.path.split("F:/study/python/study/1.txt"))

    # os.rename('test.py','test1.py') # 对文件的重命名 文件需要存在才可以

    # 列出当前目录下所有目录
    listdirs = [x for x in os.listdir("F:\study\python\study") if os.path.isfile(os.path.join("F:\study\python\study", x)) == 1]


    # 列出指定目录下所有py结尾的文件

    listdirs2 =  [x for x in os.listdir("F:\study\python\study/01-Base") if os.path.isfile(os.path.join("F:\study\python\study/01-Base", x)) and os.path.splitext(x)[1] == ".py"]

    # print(os.path.isfile("E:\export\export_data_1624860459878.txt"))
    print(os.listdir("E:\export"))
    print(listdirs)
    print(listdirs2)

    # print(s)

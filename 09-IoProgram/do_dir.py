# -*- coding:utf-8 -*-
# @FileName  :do_dir.py
# @Time      :2022/5/13 15:50
# @Author    :dzz
# @Function  :
from datetime import datetime
import os

if __name__ == "__main__":
    path = "E:\export"

    for f in os.listdir(path):
        fPath = os.path.join(path, f)
        fsize = os.path.getsize(fPath)

        mtime = datetime.fromtimestamp(os.path.getmtime(fPath)).strftime('%Y-%m-%d %H:%M')
        # flag = '/' if os.path.isdir(fPath) else ''
        # flag =
        if os.path.isdir(fPath):
            flag = '/'
        else:
            flag = ''
        print('%10d  %s  %s%s' % (fsize, mtime, f, flag))

    print("wal测试")
    for root, dirs, files in os.walk(path,topdown=False):
        print(root, dirs, files)

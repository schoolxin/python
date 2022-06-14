# -*- coding:utf-8 -*-
# @FileName  :pillowDemo1.py
# @Time      :2022/6/10 10:14
# @Author    :dzz
# @Function  :

from PIL import Image, ImageFilter
import os
if __name__ == "__main__":
    print(os.path.abspath(__file__))
    print(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    print(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
    im: Image = Image.open("hh.jpg")

    w, h = im.size
    print(f"原始大小:{w}*{h}")

    # 进行缩放
    im.thumbnail((w // 2, h // 2))

    # im.save('thumbnail.jpg', 'jpeg')

    im2 = im.filter(ImageFilter.EMBOSS)

    im2.save('blur.jpg', 'jpeg')

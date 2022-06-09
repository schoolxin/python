# -*- coding:utf-8 -*-
# @FileName  :md5Demo01.py
# @Time      :2022/6/8 18:24
# @Author    :dzz
# @Function  :
import hashlib, random


def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)


def login(username, password):
    user = db[username]
    return user.password == get_md5(password)


if __name__ == "__main__":
    db = {
        'michael': User('michael', '123456'),
        'bob': User('bob', 'abc999'),
        'alice': User('alice', 'alice2008')
    }

    print(login('michael', '123456'))

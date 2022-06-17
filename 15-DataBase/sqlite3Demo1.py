# -*- coding:utf-8 -*-
# @FileName  :sqlite3Demo1.py
# @Time      :2022/6/15 18:29
# @Author    :dzz
# @Function  :
import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')

print(db_file)
if os.path.exists(db_file):
    os.remove(db_file)

# 链接数据库
cnn = sqlite3.connect(db_file)
# 打开游标 使用游标操作数据库
curs = cnn.cursor()
curs.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
curs.execute(r"insert into user values ('A-001', 'Adam', 95)")
curs.execute(r"insert into user values ('A-002', 'Bart', 62)")
curs.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cnn.commit()
curs.close()


def get_score_in(low, high):
    curs = cnn.cursor()
    curs.execute("select name from user where score >=? and score<=? order by score asc", (low, high))

    # values = curs.fetchall()
    for row in iter(lambda: curs.fetchone(), None):
        yield row


if __name__ == "__main__":

    for value in get_score_in(60, 90):
        print(value[0])

cnn.close()

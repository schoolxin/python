# -*- coding:utf-8 -*-
# @FileName  :use_datetime.py
# @Time      :2022/6/7 17:48
# @Author    :dzz
# @Function  :
import re
from datetime import datetime, timezone, timedelta


## t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')

def to_timestamp(dt_str, tz_str):
    dt_date = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')

    re1 = re.compile(r"UTC([+-])(\d){1,2}(:00)")

    match_info = re1.match(tz_str)

    operate = match_info[1]

    hour = int(match_info[2])
    print(dt_date,operate,hour,match_info[3])
    if operate == '-':
        dt_date = dt_date - timedelta(hours=hour)
    else:
        dt_date = dt_date + timedelta(hours=hour)

    print(dt_date)

    print(dt_date.timestamp())


if __name__ == "__main__":
    to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')

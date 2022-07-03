# -*- coding:UTF-8 -*-
# file_name     :factorialDemo01.py
# create_date   :2022/7/3 
# author         : dzz
def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)

print(fac(10))

if __name__ == '__main__':
    pass

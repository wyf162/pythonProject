# _*_ coding: utf-8 _*_
# @Time : 4/23/22 10:00 PM 
# @Author : yefe
# @File : 01


def change_ibit_one2zero(x, i):
    nx = x ^ (1 << i)
    print(format(x, '0=4b'))
    print(format(nx, '0=4b'))
    return nx


if __name__ == '__main__':
    x = 10
    i = 3
    y = change_ibit_one2zero(x, i)
    print(y)

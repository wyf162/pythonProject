# -*- coding : utf-8 -*-
# @Time: 2023/10/9 22:37
# @Author: yefei.wang
# @File: c.py

# import sys

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()

for _tcn_ in range(tcn):
    n = I()
    if n % 3 == 0:
        x = 1
        y = 4
        z = n - x - y
        if z <= 0 or z == x or z == y:
            print('NO')
        else:
            print('YES')
            print(' '.join(map(str, [x, y, z])))
    else:
        x = 1
        y = 2
        z = n - x - y
        if z <= 0 or z == x or z == y:
            print('NO')
        else:
            print('YES')
            print(' '.join(map(str, [x, y, z])))

# -*- coding : utf-8 -*-
# @Time: 2023/11/4 20:03
# @Author: yefei.wang
# @File: B.py

import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

B = I()
x = 1
while True:
    y = pow(x, x)
    if y < B:
        x += 1
    elif y == B:
        exit(print(x))
    else:
        exit(print(-1))

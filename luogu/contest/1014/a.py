# -*- coding : utf-8 -*-
# @Time: 2023/10/14 14:33
# @Author: yefei.wang
# @File: c.py

import sys

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
a = [LI() for _ in range(n)]
t = I()

s = 0
for i in range(n):
    factor = 100 // a[i][0]
    s += a[i][1] * factor

if s >= t:
    print('Already Au.')
    exit(0)

for i in range(n):
    factor = 100 // a[i][0]
    d = a[i][0] - a[i][1]
    if d * factor + s < t:
        print('NaN')
    else:
        print((t - s + factor - 1) // factor)

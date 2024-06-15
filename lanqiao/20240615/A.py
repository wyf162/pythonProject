# -*- coding : utf-8 -*-
# @Time: 2024/6/15 19:01
# @Author: yefei.wang
# @File: A.py

import os
import sys


def divisors(M):
    d = []
    i = 1
    while M >= i ** 2:
        if M % i == 0:
            d.append(i)
            if i ** 2 != M:
                d.append(M // i)
        i = i + 1
    return d


# 请在此输入您的代码
sys.stdin = open('../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    x, y = MI()
    if x % y == 0 or x % y == 0:
        print(0)
        continue

    if x > y:
        x, y = y, x

    d = y - x
    divs = divisors(d)
    divs.sort()
    for div in divs:
        if div >= x:
            print(div - x)
            break
    else:
        print(-1)

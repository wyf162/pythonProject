# -*- coding : utf-8 -*-
# @Time: 2023/11/11 18:54
# @Author: yefei.wang
# @File: B.py

import os
import sys

# 请在此输入您的代码
sys.stdin = open('../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
a = LI()


def f1(x):
    if x >= 500:
        return 500 - x // 10
    return x


def f2(x):
    if x >= 1000:
        return x - 150
    return x


def f3(x):
    if x == 1111:
        return 0
    return x - x // 20


rst = 0
for x in a:
    x1 = f1(x)
    x2 = f2(x)
    x3 = f3(x)
    rst += min(x1, x2, x3)
print(rst)
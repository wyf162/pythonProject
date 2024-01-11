# -*- coding : utf-8 -*-
# @Time: 2023/10/10 0:01
# @Author: yefei.wang
# @File: C.py
import math


def next_string(s, m):
    stk = []
    for i in range(len(s)):
        while stk and stk[-1] > s[i] and m > 0:
            stk.pop()
            m -= 1
        stk.append(s[i])
        i += 1
    return stk


import sys

sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    ss = input()
    k = I()
    n = len(ss)
    m = 0
    while n < k:
        k -= n
        n -= 1
        m += 1
    nss = next_string(ss, m)
    rst = nss[k - 1]
    print(rst, end='')

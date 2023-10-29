# -*- coding : utf-8 -*-
# @Time: 2023/10/10 0:01
# @Author: yefei.wang
# @File: c.py
import math


def next_string(s, m):
    s = list(s)
    stk = []
    for i in range(n):
        while stk and stk[-1] > s[i] and m > 0:
            stk.pop()
            m -= 1
        stk.append(s[i])
        i += 1
    return stk


import sys

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    ss = input()
    k = I()
    n = len(ss)
    l, r = 1, n
    idx = 0
    while l <= r:
        m = (l + r) // 2
        if (n + m) * (n - m - 1) < k:
            idx = m
            r = m - 1
        else:
            l = m + 1
    m = int(math.sqrt(n * n + n - 2 * k + 2 * idx + 0.25) + 0.6)
    nss = next_string(ss, n - m)
    rst = nss[idx - 1]
    print(rst, end='')

# -*- coding : utf-8 -*-
# @Time: 2023/11/17 22:53
# @Author: yefei.wang
# @File: C.py

import sys

# sys.stdin = open('./../../../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    a = LI()
    ans = a[0]
    s = a[0]
    for i in range(1, n):
        if (a[i - 1] % 2) ^ (a[i] % 2):
            s = max(s, 0)
            s += a[i]
            ans = max(ans, s)
        else:
            s = a[i]
            ans = max(ans, s)
    print(ans)

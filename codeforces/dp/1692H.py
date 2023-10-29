# -*- coding : utf-8 -*-
# @Time: 2023/10/13 21:37
# @Author: yefei.wang
# @File: 1692H.py

import sys

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    a = LI()
    hst = {x: [] for x in sorted(a)}
    for i, x in enumerate(a):
        hst[x].append(i)
    dp = [0] * n

    t, l, r = a[0], -1, 1
    mx = 1
    for k, v in hst.items():
        m = len(v)
        dp[0] = 1
        for i in range(1, m):
            dp[i] = max(1, dp[i - 1] + 1 - (v[i] - v[i - 1] - 1))
            if dp[i] > mx:
                mx = dp[i]
                t, r = k, v[i] + 1

    for i in range(r - 1, -1, -1):
        if a[i] == t:
            mx -= 1
        else:
            mx += 1
        if mx == 0:
            l = i + 1
            break

    print(t, l, r)

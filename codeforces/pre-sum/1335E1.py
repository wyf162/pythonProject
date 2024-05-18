# -*- coding : utf-8 -*-
# @Time: 2024/5/18 17:43
# @Author: yefei.wang
# @File: 1335E1.py

import sys

sys.stdin = open('../input.txt', 'r')
# sys.stdout = open('./../output.txt', 'w')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    a = LI()
    f = [[0] * 26 for i in range(n + 1)]
    for i in range(n):
        x = a[i] - 1
        for j in range(26):
            f[i + 1][j] = f[i][j] + int(j == x)
    ans = max(f[n][i] for i in range(26))
    for i in range(n):
        for j in range(i + 1, n):
            mid = 0
            for x in range(26):
                mid = max(mid, f[j][x] - f[i][x])
            left = 0
            for x in range(26):
                left = max(left, min(f[i][x], f[n][x] - f[j][x]))
            ans = max(ans, left + mid + left)
    print(ans)

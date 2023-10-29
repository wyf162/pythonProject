# -*- coding : utf-8 -*-
# @Time: 2023/10/18 20:24
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
    ans = 1
    for i in range(n):
        for j in range(i + 1, n):
            for x in range(26):
                for y in range(26):
                    v1 = f[i][x]
                    v2 = f[j][y] - f[i][y]
                    v3 = f[n][x] - f[j][x]
                    if x != y and (v1 == 0 or v3 == 0):
                        continue
                    if x == y:
                        val = v1 + v2 + v3
                    else:
                        val = v2 + 2 * min(v1, v3)
                    if val > ans:
                        ans = val
                    if ans == n:
                        break
                        # print(i, j, x+1, y+1)
    print(ans)

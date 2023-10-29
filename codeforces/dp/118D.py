# -*- coding : utf-8 -*-
# @Time: 2023/10/10 20:07
# @Author: yefei.wang
# @File: 118D.py
import sys
from collections import Counter

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))
mod = 10 ** 9 + 7

n1, n2, k1, k2 = MI()
# (x, y, 0 or 1, c)
mod = 10 ** 8
dp = Counter()

dp[(0, 0, 0)] = [1] + [0] * k1
# dp[(0, 0, 1)] = [1] + [0] * k2
ans = 0

for k in range(1, n1 + n2 + 1):
    for j in range(max(k, n2 + 1)):
        i = k - j
        if (i - 1, j, 0) in dp:
            # footman + footman
            for x in range(k1):
                if (i, j, 0) not in dp:
                    dp[(i, j, 0)] = [0] * (k1 + 1)
                dp[(i, j, 0)][x + 1] += dp[(i - 1, j, 0)][x]
                dp[(i, j, 0)][x + 1] %= mod
        if (i - 1, j, 1) in dp:
            # horseman + footman
            for x in range(0, k2 + 1):
                if (i, j, 0) not in dp:
                    dp[(i, j, 0)] = [0] * (k1 + 1)
                dp[(i, j, 0)][1] += dp[(i - 1, j, 1)][x]
                dp[(i, j, 0)][1] %= mod
        if (i, j - 1, 0) in dp:
            # footman + horseman
            for x in range(k1 + 1):
                if (i, j, 1) not in dp:
                    dp[(i, j, 1)] = [0] * (k2 + 1)
                dp[(i, j, 1)][1] += dp[(i, j - 1, 0)][x]
                dp[(i, j, 1)][1] %= mod
        if (i, j - 1, 1) in dp:
            # horseman + horseman
            for x in range(0, k2):
                if (i, j, 1) not in dp:
                    dp[(i, j, 1)] = [0] * (k2 + 1)
                dp[(i, j, 1)][x + 1] += dp[(i, j - 1, 1)][x]
                dp[(i, j, 1)][x + 1] %= mod

for k, v in dp.items():
    if k[0] == n1 and k[1] == n2:
        ans += sum(dp[k])
        ans %= mod
print(ans)

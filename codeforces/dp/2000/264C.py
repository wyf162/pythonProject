# -*- coding: utf-8 -*-
# @Time: 2024/6/6 9:09
# @Author: yfwang
# @File: 264C.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353
inf = 10 ** 18

tcn = 2
for _tcn_ in range(tcn):
    n, q = MI()
    values = LI()
    colors = LI()
    queries = [LI() for _ in range(q)]

    for a, b in queries:
        dp = [-inf] * (n + 3)
        mx1 = n + 1
        mx2 = n + 2

        for i in range(n):
            c = colors[i]
            dp[c] = max(dp[c] + a * values[i], b * values[i], dp[c])
            if mx1 == c:
                dp[c] = max(dp[mx2] + b * values[i], dp[c])
            else:
                dp[c] = max(dp[mx1] + b * values[i], dp[c])

            if mx1 == c:
                continue
            else:
                if dp[c] > dp[mx1]:
                    mx2 = mx1
                    mx1 = c
                elif dp[c] > dp[mx2]:
                    mx2 = c

        print(max(dp[mx1], 0))

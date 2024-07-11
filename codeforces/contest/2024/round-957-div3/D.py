# -*- coding : utf-8 -*-
# @Time: 2024/7/11 22:52
# @Author: yefei.wang
# @File: D.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353
inf = 10 ** 9

tcn = I()
for _tcn_ in range(tcn):
    n, m, k = MI()
    s = 'L' + input() + 'L'
    dp = [-inf] * (n + 2)
    dp[0] = k
    for i in range(1, n + 2):
        if s[i] == 'C':
            dp[i] = -inf
            continue
        for j in range(max(0, i - m), i):
            if s[j] == 'L' or j + 1 == i:
                dp[i] = max(dp[i], dp[j])
        if s[i] == 'W':
            dp[i] -= 1
    YN(dp[-1] >= 0)

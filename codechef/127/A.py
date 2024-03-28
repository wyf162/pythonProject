# -*- coding : utf-8 -*-
# @Time: 2024/3/27 22:31
# @Author: yefei.wang
# @File: A.py

import sys
from math import inf

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

N = 2 * 10 ** 5 + 5
dp = [inf] * N
dp[1] = 1
dp[2] = 2
tot = 3
for i in range(3, N):
    dp[i] = tot + 1
    tot += dp[i]
    if tot > 10** 9:
        break

tcn = I()
for _tcn_ in range(tcn):
    n, k, x = MI()
    YN(x >= dp[k])

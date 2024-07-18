# -*- coding: utf-8 -*-
# @Time: 2024/7/18 11:02
# @Author: yfwang
# @File: 156C.py

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
fmax = lambda x, y: x if x > y else y

dp = [[0] * 2501 for _ in range(101)]
dp[0][0] = 1

for i in range(1, 101):

    for j in range(2500, -1, -1):
        for k in range(26):
            if j - k < 0:
                break
            dp[i][j] += dp[i - 1][j - k]
            if dp[i][j] >= mod:
                dp[i][j] -= mod

tcn = I()
for _tcn_ in range(tcn):
    s = input()
    n = len(s)
    m = 0
    for c in s:
        m += ord(c) - ord('a')
    ans = dp[n][m] - 1
    if ans < 0:
        ans += mod
    print(ans)

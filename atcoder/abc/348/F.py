# -*- coding : utf-8 -*-
# @Time: 2024/4/7 9:14
# @Author: yefei.wang
# @File: F.py

import sys

input = lambda: sys.stdin.readline().rstrip('\r\n')
sys.stdin = open('./../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
Yn = lambda x: print('Yes' if x else 'No')
mod = 1000000007
mod2 = 998244353

n, m = LI()
mtx = [LI() for _ in range(n)]

dp = [0] * n
for j in range(m):
    d = [0] * 1000
    for i in range(n):
        dp[i] ^= d[mtx[i][j]]
        d[mtx[i][j]] |= 1 << i
ans = 0
for i in range(n):
    for j in range(i):
        ans += (dp[i] >> j) & 1
print(ans)

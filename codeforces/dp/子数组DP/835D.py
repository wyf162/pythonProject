# -*- coding: utf-8 -*-
# @Time: 2024/5/27 11:22
# @Author: yfwang
# @File: 835D2.py
# Used: 1343 ms, 395336 KB
# palindromic

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

tcn = 1
for _tcn_ in range(tcn):
    s = input()
    n = len(s)
    ans = [0] * (n + 1)
    f = [0] * (n * n)

    idx = lambda i, j: i * n + j

    for i in range(n):
        f[idx(i, i)] = 1

    for k in range(1, n):
        c = (k + 1) // 2
        for i in range(n - k):
            if s[i] == s[i + k] and (k == 1 or f[idx(i + 1, i + k - 1)]):
                f[idx(i, i + k)] = f[idx(i, i + c - 1)] + 1

    ans = [0] * (n + 1)
    for i in range(n):
        for j in range(n):
            ans[f[idx(i, j)]] += 1
    for i in range(n - 1, -1, -1):
        ans[i] += ans[i + 1]
    print(*ans[1:])

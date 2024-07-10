# -*- coding: utf-8 -*-
# @Time: 2024/7/10 10:44
# @Author: yfwang
# @File: 489D.py

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
    n, m = MI()
    g = [[] for _ in range(n)]
    for i in range(m):
        u, v = GMI()
        g[u].append(v)

    cnt = [0] * n
    ans = 0
    for i in range(n):
        for j in g[i]:
            for k in g[j]:
                cnt[k] += 1
        for j in range(n):
            if i != j:
                ans += cnt[j] * (cnt[j] - 1) // 2
            cnt[j] = 0
    print(ans)

# -*- coding : utf-8 -*-
# @Time: 2024/4/20 12:06
# @Author: yefei.wang
# @File: 1615D.py
# https://codeforces.com/problemset/problem/1615/D

import sys

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

tcn = I()
for _tcn_ in range(tcn):
    n, m = MI()
    g = [[] for _ in range(n)]
    for _ in range(n-1):
        u, v, w = GMI()
        w += 1
        g[u].append([v, w])
        g[v].append([u, w])
    hst = dict()
    for i in range(m):
        u, v, p = GMI()
        p += 1
        hst[(u, v)] = p
        hst[(v, u)] = p

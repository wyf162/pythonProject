# -*- coding : utf-8 -*-
# @Time: 2024/5/11 13:20
# @Author: yefei.wang
# @File: 1598D.py

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

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    edges = []
    g1 = [[] for _ in range(n)]
    g2 = [[] for _ in range(n)]
    for i in range(n):
        a, b = GMI()
        edges.append((a, b))
        g1[a].append(b)
        g2[b].append(a)

    ans = 0
    for a, b in edges:
        x1 = len(g1[a]) - 1
        x2 = len(g2[b]) - 1
        ans += x1 * x2

    ans = n * (n - 1) * (n - 2) // 6 - ans
    print(ans)

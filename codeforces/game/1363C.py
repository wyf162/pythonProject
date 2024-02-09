# -*- coding : utf-8 -*-
# @Time: 2024/2/9 14:45
# @Author: yefei.wang
# @File: 1363C.py

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
    n, k = MI()
    k -= 1
    g = [[] for _ in range(n)]
    deg = [0] * n
    for _ in range(n - 1):
        u, v = GMI()
        g[u].append(v)
        g[v].append(u)
        deg[u] += 1
        deg[v] += 1
    if deg[k] == 1 or n == 1 or n % 2 == 0:
        print('Ayush')
    else:
        print('Ashish')

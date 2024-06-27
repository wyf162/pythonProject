# -*- coding : utf-8 -*-
# @Time: 2024/6/27 20:04
# @Author: yefei.wang
# @File: 1085D.py

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
    n, s = MI()
    deg = [0] * n
    for i in range(n-1):
        u, v = GMI()
        deg[u] += 1
        deg[v] += 1
    c = deg.count(1)
    ans = s / c * 2
    print(ans)

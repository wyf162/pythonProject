# -*- coding: utf-8 -*-
# @Time: 2024/6/26 13:11
# @Author: yfwang
# @File: 1009D.py
import math
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

tcn = 2
for _tcn_ in range(tcn):
    n, m = MI()
    M = m
    if m < n - 1:
        print("Impossible")
        continue
    edges = []
    for v in range(2, n + 1):
        edges.append((1, v))
    m -= n - 1
    for x in range(2, n + 1):
        if m == 0:
            break
        for d in range(1, x):
            if math.gcd(x, x+d) > 1:
                continue
            for y in range(x + d, n + 1, x):
                edges.append((x, y))
                m -= 1
                if m == 0:
                    break
            if m == 0:
                break
    if len(edges) < M:
        print("Impossible")
    else:
        print("Possible")
        for i in range(M):
            print(*edges[i])

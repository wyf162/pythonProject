# -*- coding : utf-8 -*-
# @Time: 2023/10/22 13:04
# @Author: yefei.wang
# @File: g.py


import sys

sys.stdin = open('../../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
a = LI()
g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = MI()
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)


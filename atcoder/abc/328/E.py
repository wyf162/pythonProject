# -*- coding : utf-8 -*-
# @Time: 2023/11/11 20:29
# @Author: yefei.wang
# @File: E.py

import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

N, M, K = MI()
g = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = MI()
    w %= K
    g[u].append([v, w])
    g[v].append([u, w])


# -*- coding : utf-8 -*-
# @Time: 2024/7/20 12:19
# @Author: yefei.wang
# @File: 954D.py
# shortest paths

import sys
from collections import deque

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

tcn = 3
for _tcn_ in range(tcn):
    n, m, s, t = MI()
    s -= 1
    t -= 1
    g = [[] for _ in range(n)]
    for i in range(m):
        u, v = GMI()
        g[u].append(v)
        g[v].append(u)

    dist1 = [-1] * n
    q = deque()
    q.append(s)
    dist1[s] = 0
    while q:
        for _ in range(len(q)):
            x = q.popleft()
            for y in g[x]:
                if dist1[y] >= 0:
                    continue
                dist1[y] = dist1[x] + 1
                q.append(y)
    # print(dist1)

    dist2 = [-1] * n
    q = deque()
    q.append(t)
    dist2[t] = 0
    while q:
        for _ in range(len(q)):
            x = q.popleft()
            for y in g[x]:
                if dist2[y] >= 0:
                    continue
                dist2[y] = dist2[x] + 1
                q.append(y)
    # print(dist2)

    ans = n * (n - 1) // 2 - m
    for i in range(n):
        for j in range(i+1, n):
            if dist1[i] + 1 + dist2[j] < dist1[t]:
                ans -= 1
            elif dist1[j] + 1 + dist2[i] < dist1[t]:
                ans -= 1
    print(ans)

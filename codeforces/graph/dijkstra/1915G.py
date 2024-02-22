# -*- coding: utf-8 -*-
# @Time: 2024/2/22 13:35
# @Author: yfwang
# @File: 1915G.py
# https://codeforces.com/problemset/problem/1915/G

import sys
from heapq import heappop, heappush

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353
inf = float('inf')

tcn = I()
for _tcn_ in range(tcn):
    n, m = MI()
    edges = [LI() for _ in range(m)]
    nums = LI()
    g = [[] for _ in range(n)]
    for u, v, w in edges:
        u -= 1
        v -= 1
        g[u].append([v, w])
        g[v].append([u, w])

    dist = [[inf for _ in range(n)] for _ in range(1002)]

    h = [(0, 0, nums[0])]
    while h:
        v, x, c = heappop(h)
        if dist[c][x] <= v:
            continue
        dist[c][x] = v
        for y, w in g[x]:
            heappush(h, (v + c * w, y, min(nums[y], c)))
    ans = inf
    for i in range(1002):
        ans = min(ans, dist[i][-1])
    print(ans)

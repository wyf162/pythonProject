# -*- coding: utf-8 -*-
# @Time: 2024/5/27 9:52
# @Author: yfwang
# @File: 687A.py
# https://codeforces.com/problemset/problem/687/A
# bipartite

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
    for _ in range(m):
        u, v = GMI()
        g[u].append(v)
        g[v].append(u)

    color = [0] * n
    ans = True
    for i in range(n):
        if color[i] != 0:
            continue
        q = [i]
        while q:
            x = q.pop()
            if color[x] == 0:
                color[x] = 1
            for y in g[x]:
                if color[y] == 0:
                    color[y] = -color[x]
                    q.append(y)
                else:
                    if color[y] == -color[x]:
                        continue
                    else:
                        ans = False
                        break
            if ans is False:
                break
        if ans is False:
            break
    if ans is False:
        print(-1)
    else:
        vertex1 = [i for i, c in enumerate(color) if c == 1]
        vertex2 = [i for i, c in enumerate(color) if c == -1]
        print(len(vertex1))
        print(*[x+1 for x in vertex1])
        print(len(vertex2))
        print(*[x+1 for x in vertex2])

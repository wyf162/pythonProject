# -*- coding : utf-8 -*-
# @Time: 2023/11/4 20:13
# @Author: yefei.wang
# @File: D.py

import sys

sys.setrecursionlimit(10 ** 6)

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

N, M = MI()
A = LI()
B = LI()

g = [[] for _ in range(N)]

for x, y in zip(A, B):
    if x == y:
        exit(print('No'))
    x -= 1
    y -= 1
    g[x].append(y)
    g[y].append(x)

color = [0] * N


def dfs(x, fa):
    for y in g[x]:
        if color[y] == 0:
            color[y] = -color[x]
        else:
            if color[y] + color[x] == 0:
                continue
            else:
                exit(print('No'))
        if y != fa:
            dfs(y, x)


for i in range(N):
    if color[i] == 0:
        color[i] = 1
        dfs(i, -1)

exit(print('Yes'))

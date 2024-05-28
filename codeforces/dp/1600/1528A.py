# -*- coding : utf-8 -*-
# @Time: 2024/1/22 22:34
# @Author: yefei.wang
# @File: 1528A.py
# https://codeforces.com/problemset/problem/1528/A
# trees

import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())

inf = float('inf')

t = I()
for _ in range(t):
    n = I()
    lefts = []
    rights = []
    for _ in range(n):
        l, r = MI()
        lefts.append(l)
        rights.append(r)

    path = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = GMI()
        path[u].append(v)
        path[v].append(u)

    parent = [-1] * n
    stack = [0]
    order = []
    while stack:
        u = stack.pop()
        for v in path[u]:
            if v and parent[v] == -1:
                parent[v] = u
                stack.append(v)
                order.append(v)

    res0 = [0] * n
    res1 = [0] * n
    order.reverse()
    for u in order:
        res0[parent[u]] += max(abs(lefts[parent[u]] - lefts[u]) + res0[u],
                               abs(lefts[parent[u]] - rights[u]) + res1[u])
        res1[parent[u]] += max(abs(rights[parent[u]] - lefts[u]) + res0[u],
                               abs(rights[parent[u]] - rights[u]) + res1[u])
    print(max(res0[0], res1[0]))

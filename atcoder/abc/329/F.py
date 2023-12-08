# -*- coding : utf-8 -*-
# @Time: 2023/11/18 20:35
# @Author: yefei.wang
# @File: F.py

import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, q = MI()
c = LI()
qs = [LI() for _ in range(q)]

fa = [i for i in range(n)]

ss = [set() for i in range(n + 1)]
for i, x in enumerate(c):
    ss[i].add(x)

for a, b in qs:
    a, b = a - 1, b - 1
    if ss[fa[a]] and ss[fa[b]]:
        if len(ss[fa[a]]) < len(ss[fa[b]]):
            for x in ss[fa[a]]:
                ss[fa[b]].add(x)
        else:
            for x in ss[fa[b]]:
                ss[fa[a]].add(x)
            fa[b] = fa[a]

        fa[a] = n
    elif ss[fa[a]] and not ss[fa[b]]:
        fa[b] = fa[a]
        fa[a] = n

    print(len(ss[fa[b]]))

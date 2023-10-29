# -*- coding : utf-8 -*-
# @Time: 2023/10/7 20:36
# @Author: yefei.wang
# @File: d.py

import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
a = [LI() for _ in range(n)]
a.sort(key=lambda x: x[0])
# size count
hst = {s: c for s, c in a}
vis = set()
ans = 0

for i in range(n):
    s, c = a[i]
    if s in vis:
        continue

    while c > 0:
        if c % 2:
            ans += 1
        c //= 2
        s *= 2
        if s in hst:
            c += hst[s]
            vis.add(s)

print(ans)

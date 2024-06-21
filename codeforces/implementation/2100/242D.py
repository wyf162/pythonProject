# -*- coding: utf-8 -*-
# @Time: 2024/6/21 11:13
# @Author: yfwang
# @File: 242D.py
# graphs

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

n, m = MI()
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = GMI()
    g[u].append(v)
    g[v].append(u)

deg = LI()
q = []
for i, d in enumerate(deg):
    if d == 0:
        q.append(i)

ans = []
while q:
    x = q.pop()
    ans.append(x)
    deg[x] -= 1
    for y in g[x]:
        deg[y] -= 1
        if deg[y] == 0:
            q.append(y)

print(len(ans))
print(' '.join(str(x+1) for x in ans))
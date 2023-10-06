# -*- coding : utf-8 -*-
# @Time: 2023/10/5 20:39
# @Author: yefei.wang
# @File: P7167.py

import sys

sys.stdin = open('./../input.txt', 'r')

input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, q = MI()
disks = [LI() for _ in range(n)]
disks.insert(0, [])
queries = [LI() for _ in range(q)]

fa = [0 for _ in range(n + 1)]
stk = []
for i in range(1, n + 1):
    di, ci = disks[i]
    while stk and disks[stk[-1]][0] < di:
        j = stk.pop()
        fa[j] = i
    stk.append(i)

# print(fa)
B = 17
f = [[0 for j in range(B)] for i in range(n + 1)]
g = [[0 for j in range(B)] for i in range(n + 1)]
for i in range(1, n + 1):
    f[i][0] = fa[i]
    g[i][0] = disks[i][1]

for k in range(1, B):
    for i in range(1, n + 1):
        f[i][k] = f[f[i][k - 1]][k - 1]
        g[i][k] = g[i][k - 1] + g[f[i][k - 1]][k - 1]

for r, v in queries:
    ci = r
    cv = v
    for b in range(B-1, -1, -1):
        if cv > g[ci][b]:
            cv -= g[ci][b]
            ci = f[ci][b]
    print(ci)

# -*- coding : utf-8 -*-
# @Time: 2024/6/23 13:18
# @Author: yefei.wang
# @File: 1738D.py
# https://codeforces.com/contest/1738/problem/D
# permutation

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

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    B = LI()
    cnt = 0
    to = [[] for i in range(n + 10)]
    for i in range(n):
        if B[i] > i + 1:
            cnt += 1
        to[B[i]].append(i + 1)

    k = cnt
    todo = []
    if len(to[0]) != 0:
        todo.append(0)
    else:
        todo.append(n + 1)

    ans = []
    while todo:
        v = todo.pop()
        if 1 <= v <= n:
            ans.append(v)
        p = []
        q = []
        for u in to[v]:
            if len(to[u]) == 0:
                p.append(u)
            else:
                q.append(u)
        for u in q + p:
            todo.append(u)

    print(k)
    print(*ans)

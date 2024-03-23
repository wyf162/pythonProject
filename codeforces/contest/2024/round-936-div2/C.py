# -*- coding : utf-8 -*-
# @Time: 2024/3/22 23:14
# @Author: yefei.wang
# @File: C.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n, k = MI()
    g = [[] for _ in range(n)]
    for i in range(n - 1):
        u, v = GMI()
        g[u].append(v)
        g[v].append(u)

    fa = [-1] * n
    dfs = []
    stk = [0]
    fa[0] = n
    while stk:
        x = stk.pop()
        dfs.append(x)
        for y in g[x]:
            if fa[y] == -1:
                fa[y] = x
                stk.append(y)


    def check(mid):
        sz = [0] * n
        cut_edge_cnt = 0
        for x in dfs[::-1]:
            sz[x] += 1
            if sz[x] >= mid:
                cut_edge_cnt += 1
                sz[x] = 0
            elif fa[x] < n:
                sz[fa[x]] += sz[x]
        if sz[0] >= mid:
            return cut_edge_cnt
        else:
            return cut_edge_cnt - 1


    L, R = 1, n
    ans = 1
    while L <= R:
        m = (L + R) // 2
        v = check(m)
        # print(L, R, m, v)
        if v >= k:
            ans = m
            L = m + 1
        else:
            R = m - 1
    print(ans)

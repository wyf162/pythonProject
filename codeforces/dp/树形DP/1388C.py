# -*- coding : utf-8 -*-
# @Time: 2024/2/8 20:49
# @Author: yefei.wang
# @File: 1388C.py

import sys

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

tcn = I()
for _tcn_ in range(tcn):
    n, m = MI()
    nums1 = LI()
    nums2 = LI()
    edges = [LGMI() for _ in range(n - 1)]
    g = [[] for _ in range(n)]
    for u, v in edges:
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
    fa[0] = -1
    size = [0] * n
    for x in dfs[::-1]:
        size[x] += nums1[x]
        if fa[x] >= 0:
            size[fa[x]] += size[x]
    # print(size)

    dp = [0] * n
    dpb = [0] * n
    ans = True
    for x in dfs[::-1]:
        # a - b = nums2[x]
        # a + b = size[x]
        aa = size[x] + nums2[x]
        if aa % 2:
            ans = False
            break
        a = aa // 2
        b = a - nums2[x]
        if b < 0 or a < 0 or a > size[x] or b > size[x]:
            ans = False
            break
        if len(g[x]) > 1 or fa[x] == -1:
            ca = a - dp[x]
            cb = b - dpb[x]
            if ca < 0:
                ans = False
                break
        if fa[x] >= 0:
            dp[fa[x]] += a
            dpb[fa[x]] += b
    YN(ans)

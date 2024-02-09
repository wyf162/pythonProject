# -*- coding : utf-8 -*-
# @Time: 2024/2/8 19:47
# @Author: yefei.wang
# @File: 1401D.py

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
    n = I()
    edges = [LGMI() for _ in range(n - 1)]
    m = I()
    nums = LI()
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
    # print(dfs)

    size = [0] * n
    for x in dfs[::-1]:
        size[x] += 1
        if fa[x] >= 0:
            size[fa[x]] += size[x]
    cnt = []
    for x in dfs[1:]:
        cnt.append(size[x] * (n - size[x]))
    if len(nums) < n - 1:
        nums = nums + [1] * (n - 1 - len(nums))
    cnt.sort()
    nums.sort()
    for j in range(n - 1, m):
        nums[n - 2] *= nums[j]
        nums[n - 2] %= mod
    rst = 0
    for i in range(n - 1):
        rst += nums[i] * cnt[i]
        rst %= mod
    print(rst)

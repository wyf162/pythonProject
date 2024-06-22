# -*- coding : utf-8 -*-
# @Time: 2024/6/22 11:39
# @Author: yefei.wang
# @File: 1033C.py

import sys
from functools import cache

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = 2
for _tcn_ in range(tcn):
    n = I()
    A = [0] + LI()
    ans = [False] * (n + 1)


    @cache
    def dfs(i):
        ret = False
        for j in range(i - A[i], 0, -A[i]):
            if A[j] > A[i]:
                ret |= dfs(j)
        for j in range(i + A[i], n + 1, A[i]):
            if A[j] > A[i]:
                ret |= dfs(j)
        return ~ret


    for i in range(1, n + 1):
        ans[i] = dfs(i)

    rets = ['B' if ans[i] else 'A' for i in range(1, n + 1)]

    print(''.join(rets))

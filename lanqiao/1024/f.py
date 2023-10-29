# -*- coding : utf-8 -*-
# @Time: 2023/10/24 22:04
# @Author: yefei.wang
# @File: f.py

import os
import sys
from functools import lru_cache

# 请在此输入您的代码

sys.stdin = open('../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))
mod = 998244353

L = I()
R = I()


@lru_cache(None)
def dfs(i, pre, v, is_limit, is_num):
    if i == len(s):
        if is_num and 0 < pre < v and v % pre == 0:
            return 1
        return 0
    res = 0
    if not is_num:
        res += dfs(i + 1, -1, 0, False, False)
        res %= mod

    d0 = 0 if is_num else 1
    up = int(s[i]) if is_limit else 9
    for d in range(d0, up + 1):
        res += dfs(i + 1, d, v + d, is_limit and d == up, True)
        res %= mod
    return res


s = str(L - 1)
x1 = dfs(0, -1, 0, True, False)
dfs.cache_clear()

s = str(R)
x2 = dfs(0, -1, 0, True, False)
dfs.cache_clear()
rst = x2 - x1
rst %= mod
print(rst)

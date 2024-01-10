# -*- coding : utf-8 -*-
# @Time: 2023/10/27 19:25
# @Author: yefei.wang
# @File: a.py

import sys
from functools import lru_cache

sys.stdin = open('../../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()


@lru_cache(None)
def dfs(x):
    if x <= 1:
        return x + 1
    else:
        y = (x+1) // 2
        return 2 * dfs(y - 1) - dfs(y - 2)


rst = dfs(n)
print(rst)
# -*- coding : utf-8 -*-
# @Time: 2024/4/20 20:29
# @Author: yefei.wang
# @File: E.py

import sys
from functools import lru_cache

input = lambda: sys.stdin.readline().rstrip('\r\n')
sys.stdin = open('./../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n, a, x, y = MI()


@lru_cache(None)
def f(v):
    if v == 0: return 0
    return min(f(v // a) + x,
               y + sum(f(v // i) for i in range(1, 7)) / 6)


print(f(n))

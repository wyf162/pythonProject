# -*- coding : utf-8 -*-
# @Time: 2024/6/18 21:07
# @Author: yefei.wang
# @File: 1251D.py

import sys
from heapq import nsmallest

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
    n, s = MI()
    c0 = n // 2 + 1
    segments = []
    tot = 0
    for i in range(n):
        L, R = MI()
        tot += L
        segments.append((L, R))
    s -= tot


    def check(mid):
        c1 = 0
        h = []
        for L, R in segments:
            if L >= mid:
                c1 += 1
            elif mid <= R:
                h.append(mid - L)
        if c1 >= c0:
            return True
        else:
            c2 = c0 - c1
            if len(h) >= c2 and sum(nsmallest(c2, h)) <= s:
                return True
        return False


    L = 1
    R = 10 ** 9 + 1
    while L <= R:
        mid = (L + R) // 2
        if check(mid):
            ans = mid
            L = mid + 1
        else:
            R = mid - 1
    print(ans)

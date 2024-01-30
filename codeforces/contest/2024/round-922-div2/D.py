# -*- coding : utf-8 -*-
# @Time: 2024/1/30 23:08
# @Author: yefei.wang
# @File: D.py

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
    n = I()
    A = LI()


    def check(mid):
        tot = 0
        s = 0
        for i in range(n):
            if s + A[i] <= mid:
                s += A[i]
                continue
            else:
                tot += A[i]
                s = 0
        return tot <= mid


    L, R = 1, sum(A)
    ans = R
    while L <= R:
        mid = (L + R) // 2
        if check(mid):
            ans = mid
            R = mid - 1
        else:
            L = mid + 1
    print(ans)

# -*- coding: utf-8 -*-
# @Time: 2024/7/1 9:14
# @Author: yfwang
# @File: 1840D.py

import bisect
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
    A = LI()
    A.sort()


    def check(x):
        i1 = bisect.bisect_right(A, A[0] + 2 * x)
        if i1 == n:
            return True
        i2 = bisect.bisect_right(A, A[i1] + 2 * x)
        if i2 == n:
            return True
        i3 = bisect.bisect_right(A, A[i2] + 2 * x)
        if i3 == n:
            return True
        return False


    L, R = 0, 10 ** 9
    while L <= R:
        mid = (L + R) // 2
        if check(mid):
            ans = mid
            R = mid - 1
        else:
            L = mid + 1
    print(ans)

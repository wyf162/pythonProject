# -*- coding: utf-8 -*-
# @Time: 2024/8/6 13:39
# @Author: yfwang
# @File: 1177B.py

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

A = [1] + [10 ** i for i in range(1, 13)]
B = [0] + [9 * 10 ** i for i in range(12)]

tcn = 1
for _tcn_ in range(tcn):
    k = I()
    L, R = 1, 10 ** 12
    ans = 0
    bi = 1
    while L <= R:
        mid = (L + R) // 2
        c = 0
        for i in range(1, 13):
            if mid >= A[i]:
                c += i * B[i]
            else:
                c += i * (mid - A[i - 1] + 1)
                break
        # print(c)
        if c < k:
            ans = mid
            bi = k - c
            L = mid + 1
        else:
            R = mid - 1

    print(str(ans + 1)[bi - 1])

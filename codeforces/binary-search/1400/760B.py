# -*- coding: utf-8 -*-
# @Time: 2024/5/21 8:59
# @Author: yfwang
# @File: 760B.py
# https://codeforces.com/problemset/problem/760/B

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

n, m, k = MI()

left = k
right = n - k + 1


def check(x):
    if left < x:
        tot1 = (x + x - left + 1) * left // 2
    else:
        tot1 = (x + 1) * x // 2 + left - x

    if right < x:
        tot2 = (x + x - right + 1) * right // 2
    else:
        tot2 = (x + 1) * x // 2 + right - x

    # print(tot1, tot2)
    tot = tot1 + tot2 - x
    # print(tot)
    return tot


L = 1
R = m
ans = 1
while L <= R:
    mid = (L + R) // 2
    if check(mid) <= m:
        ans = mid
        L = mid + 1
    else:
        R = mid - 1
print(ans)

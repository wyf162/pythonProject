# -*- coding: utf-8 -*-
# @Time: 2024/3/5 13:49
# @Author: yfwang
# @File: 1848C.py
# https://codeforces.com/problemset/problem/1848/C
import math
import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353


def fix(a, b):
    if a == 0 and b == 0:
        return -1
    elif a == 0:
        return 1
    elif b == 0:
        return 2
    g = math.gcd(a, b)
    a //= g
    b //= g
    if (a % 2) * (b % 2) == 1:
        return 0
    elif a % 2:
        return 2
    else:
        return 1


tcn = I()
for _tcn_ in range(tcn):
    n = I()
    A = LI()
    B = LI()
    seen = [False] * 3
    for i in range(n):
        ind = fix(A[i], B[i])
        if ind >= 0:
            seen[ind] = True
    YN(sum(seen) <= 1)

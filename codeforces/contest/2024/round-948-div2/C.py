# -*- coding : utf-8 -*-
# @Time: 2024/5/26 22:52
# @Author: yefei.wang
# @File: C.py

import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


tcn = I()
for _tcn_ in range(tcn):
    n = I()
    A = LI()
    A.sort()
    st = set(A)
    f = [defaultdict(int) for _ in range(n + 1)]
    f[0][1] = 0

    for i in range(n):
        f[i + 1][A[i]] = 1
        for k in f[i]:
            nk = lcm(k, A[i])
            f[i + 1][nk] = max(f[i + 1][nk], f[i][k] + 1)
        for k in f[i]:
            f[i + 1][k] = max(f[i + 1][k], f[i][k])
        print(len(f[i + 1]))

    ans = 0
    for k in f[n]:
        if k not in st:
            ans = max(ans, f[n][k])
    print(ans)

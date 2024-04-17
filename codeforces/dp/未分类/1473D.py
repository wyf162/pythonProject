# -*- coding : utf-8 -*-
# @Time: 2024/4/17 21:31
# @Author: yefei.wang
# @File: 1473D.py
# https://codeforces.com/contest/1473/problem/D


import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
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
    n, m = MI()
    s = list(input())
    f = [0] * (n + 1)
    fmi = [0] * (n + 1)
    fmx = [0] * (n + 1)
    for i in range(n):
        if s[i] == '-':
            f[i + 1] = f[i] - 1
        elif s[i] == '+':
            f[i + 1] = f[i] + 1
        fmi[i + 1] = min(fmi[i], f[i + 1])
        fmx[i + 1] = max(fmx[i], f[i + 1])

    gmi = [0] * (n + 1)
    gmx = [0] * (n + 1)
    for i in range(n):
        if s[n - 1 - i] == '-':
            gmi[i + 1] = min(0, gmi[i] - 1)
            gmx[i + 1] = max(0, gmx[i] - 1)
        elif s[n - 1 - i] == '+':
            gmi[i + 1] = min(0, gmi[i] + 1)
            gmx[i + 1] = max(0, gmx[i] + 1)

    for _ in range(m):
        l, r = GMI()
        mi = min(fmi[l], f[l] + gmi[n - r - 1])
        mx = max(fmx[l], f[l] + gmx[n - r - 1])
        print(mx - mi + 1)

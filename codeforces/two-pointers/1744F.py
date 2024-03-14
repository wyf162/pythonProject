# -*- coding: utf-8 -*-
# @Time: 2024/3/14 9:05
# @Author: yfwang
# @File: 1744F.py
# https://codeforces.com/problemset/problem/1744/F


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


def mex_med(a):
    a.sort()
    m = len(a)
    med = a[(m - 1) // 2]
    mex = 0
    for x in a:
        if x == mex:
            mex += 1
    # print(a, mex, med)
    return mex > med


def solve_by_brute_force(p):
    ret = 0
    for i in range(n):
        for j in range(i, n):
            ret += mex_med(p[i:j + 1])
    print(ret)


tcn = I()
for _tcn_ in range(tcn):
    n = I()
    p = LI()
    # solve_by_brute_force(p)
    p_inv = [-1] * n
    for i in range(n):
        p_inv[p[i]] = i

    mi = p_inv[0]
    mx = p_inv[0]

    ans = 1
    for i in range(2, n + 1):
        k = (i - 1) // 2
        mi = min(p_inv[k], mi)
        mx = max(p_inv[k], mx)
        mx_mi = max(mx, i-1)
        mx_mx = min(n-1, mi+i-1)
        ans += max(0, mx_mx - mx_mi + 1)
    print(ans)

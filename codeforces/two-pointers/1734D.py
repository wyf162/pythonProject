# -*- coding: utf-8 -*-
# @Time: 2024/3/19 10:15
# @Author: yfwang
# @File: 1734D.py
# https://codeforces.com/problemset/problem/1734/D

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


def solve(n, k, a):
    k -= 1
    r = k + 1
    l = k - 1
    max_r = 0
    acc = 0
    h = a[k]
    while 0 <= l:
        while r < n and 0 <= h + acc + a[r]:
            acc += a[r]
            max_r = max(max_r, acc)
            r += 1
        if 0 <= h + max_r + a[l]:
            h += a[l]
            l -= 1
        else:
            return False
    return True


tcn = I()
for _tcn_ in range(tcn):
    N, K = MI()
    nums = LI()

    if solve(N, K, nums) or solve(N, N - K + 1, list(reversed(nums))):
        YN(True)
    else:
        YN(False)

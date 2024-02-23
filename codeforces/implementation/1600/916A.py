# -*- coding: utf-8 -*-
# @Time: 2024/2/23 9:13
# @Author: yfwang
# @File: 916A.py
# https://codeforces.com/contest/916/problem/A

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

x = I()
hh, mm = MI()


def f1(h, m):
    return h * 60 + m


def f2(tm):
    return tm // 60, tm % 60


mod3 = 23 * 60 + 59


def f3(tm, dm):
    ctm = (tm - dm)
    if ctm < 0:
        ctm += 1
    return ctm % mod3


cnt = 0
while True:
    s = str(hh) + str(mm)
    if '7' in s:
        break
    hh, mm = f2(f3(f1(hh, mm), x))
    # print(hh, mm)
    cnt += 1
print(cnt)

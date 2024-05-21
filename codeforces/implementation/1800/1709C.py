# -*- coding : utf-8 -*-
# @Time: 2024/5/21 22:30
# @Author: yefei.wang
# @File: 1709C.py
# https://codeforces.com/contest/1709/problem/C
# parenthesis

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
    s = input()
    n = len(s)
    a = 0
    b = 0
    for i in range(n):
        if s[i] == '(':
            a += 1
        elif s[i] == ')':
            a -= 1
        else:
            b += 1
        if 1 - a == b:
            a = 1
            b = 0
    YN(a == b)

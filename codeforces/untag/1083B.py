# -*- coding: utf-8 -*-
# @Time: 2024/5/30 11:27
# @Author: yfwang
# @File: 1083B.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
sys.stdout = open('../output.txt', 'w')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = 1
for _tcn_ in range(tcn):
    n, k = MI()
    s = input()
    t = input()
    dp0 = [0] * n
    dp1 = [0] * n


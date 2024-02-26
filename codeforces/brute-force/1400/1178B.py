# -*- coding: utf-8 -*-
# @Time: 2024/2/26 9:20
# @Author: yfwang
# @File: 1178B.py
# https://codeforces.com/problemset/problem/1178/B

import math
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
    s = input()
    n = len(s)
    tot = [0] * n
    for i in range(1, n):
        if s[i] == 'v' and s[i-1] == 'v':
            tot[i] = tot[i-1] + 1
        else:
            tot[i] = tot[i-1]
    ans = 0
    for i in range(2, n - 2):
        if s[i] == 'o':
            ans += tot[i] * (tot[-1] - tot[i])
    print(ans)

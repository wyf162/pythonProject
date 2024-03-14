# -*- coding: utf-8 -*-
# @Time: 2024/3/14 15:29
# @Author: yfwang
# @File: 1814B.py
# https://codeforces.com/problemset/problem/1814/B

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

tcn = I()
for _tcn_ in range(tcn):
    a, b = MI()
    mx = min(max(a, b), 10 ** 5)
    ans = a + b
    for i in range(2, mx + 5):
        ans = min(ans, i - 1 + a // i + b // i + int(a % i != 0) + int(b % i != 0))
    print(ans)

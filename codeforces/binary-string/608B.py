# -*- coding: utf-8 -*-
# @Time: 2024/5/28 9:43
# @Author: yfwang
# @File: 608B.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = 2
for _tcn_ in range(tcn):
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    pre_sum = [0] * (m + 1)
    for i in range(m):
        pre_sum[i + 1] = pre_sum[i] + int(t[i])

    ans = 0
    k = m - n + 1
    for i in range(n):
        if s[i] == '0':
            ans += pre_sum[i + k] - pre_sum[i]
        else:
            ans += k - (pre_sum[i + k] - pre_sum[i])
    print(ans)

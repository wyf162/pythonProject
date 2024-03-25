# -*- coding: utf-8 -*-
# @Time: 2024/3/25 9:03
# @Author: yfwang
# @File: 1443B.py
# https://codeforces.com/problemset/problem/1443/B

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
    a, b = MI()
    s = list(int(x) for x in input())
    c = a // b
    if 1 not in s:
        print(0)
        continue

    j = s.index(1)
    s = s[j:]
    n = len(s)
    ans = 0
    activate = False
    zero = 1 << 31
    for i in range(n):
        if s[i] == 1:
            if not activate:
                activate = True
                ans += min(zero * b, a)
            zero = 0
        else:
            activate = False
            zero += 1
    print(ans)

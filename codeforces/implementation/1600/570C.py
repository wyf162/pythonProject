# -*- coding: utf-8 -*-
# @Time: 2024/7/5 9:12
# @Author: yfwang
# @File: 570C.py

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

tcn = 1
for _tcn_ in range(tcn):
    n, m = MI()
    s = list(input())

    ans = 0
    for i in range(n - 1):
        if s[i] == s[i + 1] == '.':
            ans += 1

    for _ in range(m):
        i, c = input().split()
        i = int(i) - 1
        if s[i] == c:
            print(ans)
            continue

        if c == '.':
            if i - 1 >= 0 and s[i - 1] == '.':
                ans += 1
            if i + 1 < n and s[i + 1] == '.':
                ans += 1
        elif s[i] == '.':
            if i - 1 >= 0 and s[i - 1] == '.':
                ans -= 1
            if i + 1 < n and s[i + 1] == '.':
                ans -= 1

        s[i] = c
        print(ans)

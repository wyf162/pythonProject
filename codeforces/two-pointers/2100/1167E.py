# -*- coding: utf-8 -*-
# @Time: 2024/7/18 9:19
# @Author: yfwang
# @File: 1167E.py

import bisect
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
inf = 10 ** 6

tcn = 1
for _tcn_ in range(tcn):
    n, x = MI()
    a = LI()
    mi = [n] * (x + 1)
    ma = [-1] * (x + 1)
    for i in range(n):
        ai = a[i]
        mi[ai] = min(i, mi[ai])
        ma[ai] = max(i, ma[ai])
    r = n
    y = []
    for i in range(x, -1, -1):
        if r >= ma[i]:
            r = min(r, mi[i])
            y.append(r)
        else:
            break
    else:
        ans = x * (x + 1) // 2
        print(ans)
        exit()
    y.reverse()
    l = -1
    ans = len(y) + 1
    for i in range(1, x + 1):
        if l <= mi[i]:
            ans += 1
            l = max(l, ma[i])
            c = len(y) - bisect.bisect_left(y, l)
            ans += c
        else:
            break
    print(ans)

# -*- coding: utf-8 -*-
# @Time: 2024/4/3 14:07
# @Author: yfwang
# @File: 1814C.py

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
    n, s1, s2 = MI()
    nums = LI()
    xi = [(x, i) for i, x in enumerate(nums, start=1)]
    a = []
    b = []
    xi.sort()
    while xi:
        if (len(a) + 1) * s1 < len(b) * s2 + s2:
            a.append(xi.pop()[1])
        else:
            b.append(xi.pop()[1])
    a.insert(0, len(a))
    b.insert(0, len(b))
    print(*a)
    print(*b)

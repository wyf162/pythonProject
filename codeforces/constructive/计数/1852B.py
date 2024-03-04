# -*- coding: utf-8 -*-
# @Time: 2024/3/4 14:29
# @Author: yfwang
# @File: 1852B.py
# https://codeforces.com/problemset/problem/1852/B

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
    n = I()
    nums = LI()
    xi = [(x, i) for i, x in enumerate(nums)]
    xi.sort()
    l, r, sz = 0, n - 1, n
    ans = [0] * n
    while l <= r:
        if (xi[r][0] == n - l) ^ (xi[l][0] == n - 1 - r):
            if xi[r][0] == n - l:
                ans[xi[r][1]] = sz
                sz -= 1
                r -= 1
            else:
                ans[xi[l][1]] = -sz
                l += 1
                sz -= 1
        else:
            print('NO')
            break
    else:
        print('YES')
        print(*ans)

# -*- coding: utf-8 -*-
# @Time: 2024/4/17 14:47
# @Author: yfwang
# @File: 1473C.py
# https://codeforces.com/contest/1473/problem/C
# permutation


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
    n, k = MI()
    m = n - k
    ans = list(range(1, k - m))
    ans.extend(list(range(k, k - m - 1, -1)))
    print(*ans)


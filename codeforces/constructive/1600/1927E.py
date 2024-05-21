# -*- coding: utf-8 -*-
# @Time: 2024/4/3 14:01
# @Author: yfwang
# @File: 1927E.py
# https://codeforces.com/problemset/problem/1927/E

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
    ans = [0] * n
    p = 1
    for i in range(0, k, 2):
        for j in range(i, n, k):
            ans[j] = p
            p += 1
    p = n
    for i in range(1, k, 2):
        for j in range(i, n, k):
            ans[j] = p
            p -= 1
    print(*ans)
    # for i in range(n - k + 1):
    #     print(sum(ans[i:i + k]), end=' ')
    # print()

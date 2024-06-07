# -*- coding: utf-8 -*-
# @Time: 2024/5/21 10:40
# @Author: yfwang
# @File: 420C.py
# https://codeforces.com/problemset/problem/420/C

import sys
from collections import defaultdict

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

tcn = 2
for _tcn_ in range(tcn):
    n, p = MI()
    cnt = [0] * n
    hst = defaultdict(int)
    for _ in range(n):
        x, y = GMI()
        cnt[x] += 1
        cnt[y] += 1
        if x > y: x, y = y, x
        hst[(x, y)] += 1

    ans = 0
    for u, v in hst:
        if cnt[u] + cnt[v] >= p > cnt[u] + cnt[v] - hst[(u, v)]:
            ans -= 1
    cnt.sort()
    i = 0
    for j in range(n - 1, -1, -1):
        while i < j and cnt[j] + cnt[i] < p:
            i += 1
        if i == j:
            break
        ans += j - i
    print(ans)

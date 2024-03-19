# -*- coding: utf-8 -*-
# @Time: 2024/3/19 9:20
# @Author: yfwang
# @File: 1547E.py
# https://codeforces.com/problemset/problem/1547/E


import sys
from heapq import heappop, heappush

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
    input()
    n, k = MI()
    nums1 = LI()
    nums2 = LI()

    MX = 1 << 31
    ans = [MX] * (n + 1)
    h = []
    for i, t in zip(nums1, nums2):
        heappush(h, (t, i))

    while h:
        t, i = heappop(h)
        if ans[i] == MX:
            ans[i] = t
            if i - 1 > 0:
                heappush(h, (t + 1, i - 1))
            if i + 1 <= n:
                heappush(h, (t + 1, i + 1))

    print(*ans[1:])

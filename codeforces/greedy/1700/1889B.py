# -*- coding: utf-8 -*-
# @Time: 2024/2/26 10:09
# @Author: yfwang
# @File: 1889B.py
# https://codeforces.com/problemset/problem/1889/B

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
    n, c = MI()
    nums = LI()
    h = []
    for i in range(1, n):
        heappush(h, (- nums[i] + i * c, i))

    tot = nums[0]

    ans = True
    while h:
        _, i = heappop(h)
        if tot + nums[i] >= (i+1) * c:
            tot += nums[i]
            continue
        else:
            ans = False
            break
    YN(ans)



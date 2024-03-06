# -*- coding: utf-8 -*-
# @Time: 2024/3/6 9:18
# @Author: yfwang
# @File: 1935C.py
# https://codeforces.com/contest/1935/problem/C

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
    n, m = MI()
    nums = [LI() for _ in range(n)]
    nums.sort(key=lambda x: (x[1], x[0]))

    ans = 0
    for i in range(n):
        h = []
        cur = 0
        size = 0
        for j in range(i, n):
            heappush(h, -nums[j][0])
            size += 1
            cur += nums[j][0]
            while size and nums[j][1] - nums[i][1] + cur > m:
                mx = heappop(h)
                cur += mx
                size -= 1
            ans = max(ans, size)
    print(ans)

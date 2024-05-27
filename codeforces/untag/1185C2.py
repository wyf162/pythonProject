# -*- coding : utf-8 -*-
# @Time: 2024/5/27 22:31
# @Author: yefei.wang
# @File: 1185C2.py

import sys
from heapq import heappop, heappush, heapify

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
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
    n, m = MI()
    nums = LI()
    h1 = [(-x, -i) for i, x in enumerate(nums)]
    heapify(h1)
    h2 = []

    cnt = n
    tot = sum(nums)
    ans = [0] * n
    in_h1 = [1] * n
    for i in range(n - 1, -1, -1):
        if in_h1[i]:
            cnt -= 1
            tot -= nums[i]
            in_h1[i] = 0

        while h1 and tot + nums[i] > m:
            x, j = heappop(h1)
            if -j >= i:
                continue
            tot += x
            heappush(h2, (-x, -j))
            in_h1[-j] = 0
            cnt -= 1

        while h2:
            if h2[0][1] >= i:
                heappop(h2)
                continue
            if tot + nums[i] + h2[0][0] <= m:
                x, j = heappop(h2)
                tot += x
                heappush(h1, (-x, -j))
                cnt += 1
                in_h1[j] = 1
            else:
                break
        ans[i] = max(i - cnt, 0)

    print(*ans)

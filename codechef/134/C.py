# -*- coding : utf-8 -*-
# @Time: 2024/5/15 22:44
# @Author: yefei.wang
# @File: C.py

import sys
from heapq import heappop, heappush, heappushpop

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

tcn = I()
for _tcn_ in range(tcn):
    n, q = MI()
    nums = LI()
    queries = LI()

    arr = [0] * n
    arr[0] = nums[0]
    h1 = [-nums[0]]
    h2 = []
    tot = nums[0]
    ssi = -nums[0]
    for i in range(1, n, 2):
        if i + 1 >= n:
            continue
        tot += nums[i] + nums[i + 1]
        x1 = heappushpop(h1, -nums[i])
        x2 = heappushpop(h1, -nums[i + 1])
        ssi += -nums[i] - x1
        ssi += -nums[i + 1] - x2
        arr[i + 1] = tot + 2 * ssi

        heappush(h2, -x1)
        heappush(h2, -x2)
        x3 = heappop(h2)
        heappush(h1, -x3)
        ssi += -x3

    ans = [arr[x - 1] for x in queries]
    print(*ans)

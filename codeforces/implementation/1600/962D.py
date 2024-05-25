# -*- coding : utf-8 -*-
# @Time: 2024/5/25 9:10
# @Author: yefei.wang
# @File: 962D.py

import sys
from collections import defaultdict
from heapq import heappush, heappop

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

tcn = 3
for _tcn_ in range(tcn):
    n = I()
    nums = LI()
    h = []
    groups = defaultdict(list)
    vis = set()
    for i, x in enumerate(nums):
        groups[x].append(i)
        if x not in vis:
            heappush(h, x)
            vis.add(x)

    ans = []
    while h:
        x = heappop(h)
        groups[x].sort()
        for i in range(1, len(groups[x]), 2):
            groups[2 * x].append(groups[x][i])
            if x * 2 not in vis:
                heappush(h, x * 2)
                vis.add(x * 2)

        if len(groups[x]) % 2:
            ans.append((x, groups[x][-1]))

    ans.sort(key=lambda x: x[1])
    rets = [x[0] for x in ans]
    print(len(rets))
    print(*rets)

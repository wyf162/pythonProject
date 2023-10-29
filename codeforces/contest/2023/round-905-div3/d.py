# -*- coding : utf-8 -*-
# @Time: 2023/10/22 19:35
# @Author: yefei.wang
# @File: d.py

import sys
from collections import Counter
from heapq import heappop, heappush

# sys.stdin = open('./../../../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))
YN = lambda x: print('YES' if x else 'NO')
q = I()

lpq = []
rpq = []
cnt = Counter()
n = 0

for _ in range(q):
    s = input()
    op, l, r = s.split()
    l, r = int(l), int(r)
    if op == '+':
        cnt[(l, r)] += 1
        n += 1
        heappush(lpq, (-l, r))
        heappush(rpq, (r, l))
    else:
        cnt[(l, r)] -= 1
        n -= 1
    while lpq:
        l, r = lpq[0]
        l = -l
        if cnt[(l, r)] <= 0:
            heappop(lpq)
        else:
            break

    while rpq:
        r, l = rpq[0]
        if cnt[(l, r)] <= 0:
            heappop(rpq)
        else:
            break
    if n <= 1:
        print('NO')
        continue
    mxl, _ = lpq[0]
    mxl = -mxl
    mir, _ = rpq[0]
    if mxl > mir:
        print('YES')
    else:
        print('NO')

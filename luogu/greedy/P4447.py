# -*- coding : utf-8 -*-
# @Time: 2023/10/4 19:44
# @Author: yefei.wang
# @File: P4447.py

import sys
from heapq import heappop, heappush

sys.stdin = open('./../input.txt', 'r')

input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
a = LI()
a.sort()

hst = dict()

for i in range(n):
    x = a[i]
    if x - 1 not in hst:
        hst[x] = []
        heappush(hst[x], 1)
    else:
        if hst[x-1]:
            c = heappop(hst[x-1])
        else:
            c = 0
        if x not in hst:
            hst[x] = []
            heappush(hst[x], c + 1)
        else:
            heappush(hst[x], c + 1)

ans = n
for k, v in hst.items():
    if hst[k]:
        ans = min(ans, hst[k][0])
print(ans)

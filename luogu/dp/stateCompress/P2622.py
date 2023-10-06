# -*- coding : utf-8 -*-
# @Time: 2023/10/4 15:57
# @Author: yefei.wang
# @File: P2622.py

import sys
from heapq import heappop, heappush

sys.stdin = open('./../../input.txt', 'r')

input = lambda: sys.stdin.readline().rstrip('\r\n')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
m = I()
a = [LI() for _ in range(m)]

ss = [m + 1 for _ in range(1 << n)]
ss[-1] = 0


def button(i, s):
    ns = s
    for j in range(n):
        if a[i][j] == 1:
            if s >> j & 1:
                ns &= ~(1 << j)
        elif a[i][j] == -1:
            if s >> j & 1 == 0:
                ns |= (1 << j)
    return ns


pq = []
heappush(pq, (0, (1 << n) - 1))
while pq:
    d, s = heappop(pq)
    if ss[s] < d:
        continue
    for i in range(m):
        ns = button(i, s)
        if ss[s] + 1 < ss[ns]:
            ss[ns] = ss[s] + 1
            heappush(pq, [ss[ns], ns])

print(ss[0] if ss[0] <= m else -1)

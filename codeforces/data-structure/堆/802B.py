# -*- coding : utf-8 -*-
# @Time: 2024/6/1 23:58
# @Author: yefei.wang
# @File: 802B.py

import sys
from collections import defaultdict
from heapq import heappop, heappush

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

n, c = MI()
reqs = LI()
hst = defaultdict(list)
for i, book in enumerate(reqs):
    hst[book].append(i)

for k in hst:
    hst[k].pop(0)
    hst[k].append(n)

libs = set()
cost = 0
h = []
for i, req in enumerate(reqs):
    if req in libs:
        heappush(h, (-hst[req].pop(0), req))
    else:
        if len(libs) == c:
            _, book = heappop(h)
            libs.remove(book)
        cost += 1
        libs.add(req)
        heappush(h, (-hst[req].pop(0), req))

print(cost)

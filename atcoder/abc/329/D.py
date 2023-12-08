# -*- coding : utf-8 -*-
# @Time: 2023/11/18 20:08
# @Author: yefei.wang
# @File: D.py

import sys
from collections import Counter
from heapq import heappop, heappush

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, m = MI()
a = LI()

h = []
cnt = Counter()

for i, x in enumerate(a):
    cnt[x] -= 1
    heappush(h, [cnt[x], x])
    rst = h[0][1]
    print(rst)

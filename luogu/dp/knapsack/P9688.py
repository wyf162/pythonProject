# -*- coding : utf-8 -*-
# @Time: 2023/10/2 19:58
# @Author: yefei.wang
# @File: P9688.py

import sys
from collections import defaultdict, Counter

sys.stdin = open('./../../input.txt', 'r')
input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, K = MI()
a = LI()
b = LI()

# color to left right
c2lr = defaultdict(list)
for i, c in enumerate(a):
    c2lr[c].append(i)

si = []
ei = []
for k, v in c2lr.items():
    c2lr[k] = [min(v), max(v)]
    si.append(c2lr[k][0])
    ei.append(c2lr[k][1])
si.sort()
ei.sort()

dp = {i: Counter() for i in ei}

for s in si:
    ci = a[s]
    start, end = c2lr[ci]
    for right in ei:
        if right > start:
            break
        cj = a[right]
        if cj < ci and c2lr[cj][1] < start:
            for k, v in dp[right].items():
                dp[end][k+1] = max(dp[right][k] + b[ci-1], dp[end][k+1])

    dp[end][1] = b[ci-1]

ans = 0
for e in ei:
    ans = max(ans, dp[e][K])
ans = -1 if ans == 0 else ans
print(ans)






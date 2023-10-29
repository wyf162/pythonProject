# -*- coding : utf-8 -*-
# @Time: 2023/10/21 12:31
# @Author: yefei.wang
# @File: b.py

from heapq import heappush

# sys.stdin = open('./../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, d = MI()
dists = LI()
prices = LI()

pq = []
heappush(pq, prices[0])
cost = 0
cur = 0
for i in range(1, n):
    oil = (dists[i - 1] - cur + d - 1) // d
    cur += oil * d - dists[i - 1]
    cost += oil * pq[0]

    heappush(pq, prices[i])

print(cost)

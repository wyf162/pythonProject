# -*- coding : utf-8 -*-
# @Time: 2023/10/30 20:29
# @Author: yefei.wang
# @File: d.py
import heapq
import sys

sys.stdin = open('../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, m, h = MI()
g = [[] for i in range(n)]
for _ in range(m):
    u, v, w, d = MI()
    u -= 1
    v -= 1
    g[u].append([v, w, d])
    g[v].append([u, w, d])

MX = 0x3f3f3f3f


def check(test):
    dist = [MX] * n
    vis = [False] * n
    dist[0] = 0
    q = [(0, 0)]
    while q:
        _, u = heapq.heappop(q)
        if vis[u]:
            continue
        vis[u] = True
        for v, w, d in g[u]:
            if w < test:
                continue
            if dist[v] > dist[u] + d:
                dist[v] = dist[u] + d
                heapq.heappush(q, (dist[v], v))

    return dist[-1] <= h


ok, ng = 0, 10 ** 9 + 5
ans = -1
while ok <= ng:
    test = (ok + ng) // 2
    if check(test):
        ans = test
        ok = test + 1
    else:
        ng = test - 1

print(ans)

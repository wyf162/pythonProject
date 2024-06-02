# -*- coding : utf-8 -*-
# @Time: 2024/6/2 20:25
# @Author: yefei.wang
# @File: 802C.py
# min_cost_max_flow graphs

import sys
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

oo = 2 ** 63


class Edge:
    def __init__(self, u, v, cap, cost, rev):
        self.u = u
        self.v = v
        self.cap = cap
        self.flow = 0
        self.cost = cost
        self.rev = rev


def add_edge(adj, u, v, capv, costv):
    adj[u].append(Edge(u, v, capv, costv, len(adj[v])))
    adj[v].append(Edge(v, u, 0, -costv, len(adj[u]) - 1))


def bellman_ford(adj, s):
    dist = [oo] * len(adj)
    dist[s] = 0

    for _ in range(len(adj)):
        for u in range(len(adj)):
            for e in adj[u]:
                if e.cap - e.flow > 0 and dist[e.v] > dist[e.u] + e.cost:
                    dist[e.v] = dist[e.u] + e.cost

    return dist


def dijkstra(adj, potential, s, t):
    dist, pi = [+oo] * len(adj), [None] * len(adj)

    dist[s] = 0
    heap = [(0, s)]

    while heap:
        du, u = heappop(heap)

        if dist[u] < du: continue
        if u == t: break

        for e in adj[u]:
            reduced_cost = potential[e.u] + e.cost - potential[e.v]
            if e.cap - e.flow > 0 and dist[e.v] > dist[e.u] + reduced_cost:
                dist[e.v] = dist[e.u] + reduced_cost
                heappush(heap, (dist[e.v], e.v))
                pi[e.v] = e

    return dist, pi


def min_cost_max_flow(adj, s, t, flow_limit=oo):
    min_cost, max_flow = 0, 0

    potential = bellman_ford(adj, s)

    while True:
        dist, pi = dijkstra(adj, potential, s, t)

        if dist[t] == +oo:
            break

        for v in range(len(adj)):
            # if dist[v] != +oo:
            potential[v] += dist[v]

        limit, v = +oo, t
        while v:
            e = pi[v]
            limit = min(limit, e.cap - e.flow)
            v = e.u

        v, cost = t, 0
        while v:
            e = pi[v]
            e.flow += limit
            adj[v][e.rev].flow -= limit
            cost += e.cost
            v = e.u

        if max_flow + limit >= flow_limit:
            min_cost += limit * cost
            max_flow += flow_limit - max_flow

            return min_cost, max_flow

        min_cost += limit * cost
        max_flow += limit

    return min_cost, max_flow


n, k = MI()
pre = [None] * (n + 1)
s, t = 0, 2 * n + 1
adj = [[] for _ in range(t + 1)]
a = [None] + LI()
for i in range(1, n + 1):
    add_edge(adj, i, i + n, 1, 0)
    add_edge(adj, i + n, t, 1, 0)

c = [None] + list(map(int, sys.stdin.readline().split()))

for i in range(1, n + 1):
    add_edge(adj, s, i, 1, c[a[i]])

    if pre[a[i]]:
        add_edge(adj, i - 1, pre[a[i]] + n, 1, -c[a[i]])
    pre[a[i]] = i

for i in range(1, n):
    add_edge(adj, i, i + 1, k - 1, 0)

min_cost, max_flow = min_cost_max_flow(adj, s, t)
print(min_cost)
# print(max_flow)

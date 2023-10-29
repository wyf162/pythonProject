# -*- coding : utf-8 -*-
# @Time: 2023/10/27 20:06
# @Author: yefei.wang
# @File: e.py
import copy
import math
import queue
import sys


def edmonds_karp(capacity, source, sink):
    # Computes maximum flow from source to sink using BFS.
    # Time complexity : O(V*E^2)
    # V is the number of vertices and E is the number of edges.
    vertices = len(capacity)
    ret = 0
    flow = [[0]*vertices for i in range(vertices)]
    while True:
        tmp = 0
        q = queue.Queue()
        visit = [False for i in range(vertices)]
        par = [-1 for i in range(vertices)]
        visit[source] = True
        q.put((source, 1 << 63))
        # Finds new flow using BFS.
        while q.qsize():
            front = q.get()
            idx, current_flow = front
            if idx == sink:
                tmp = current_flow
                break
            for nxt in range(vertices):
                if not visit[nxt] and flow[idx][nxt] < capacity[idx][nxt]:
                    visit[nxt] = True
                    par[nxt] = idx
                    q.put((nxt, min(current_flow, capacity[idx][nxt]-flow[idx][nxt])))
        if par[sink] == -1:
            break
        ret += tmp
        parent = par[sink]
        idx = sink
        # Update flow array following parent starting from sink.
        while parent != -1:
            flow[parent][idx] += tmp
            flow[idx][parent] -= tmp
            idx = parent
            parent = par[parent]
    return ret


sys.stdin = open('./../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
a = LI()
b = LI()
N = 2 * n + 2
adj_mtx = [[0 for _ in range(N)] for _ in range(N)]
for i in range(1, n + 1):
    adj_mtx[0][i] = 1

for i in range(n + 1, 2 * n + 1):
    adj_mtx[i][2 * n + 1] = 1

for i in range(n):
    for j in range(n):
        if math.gcd(a[i], b[j]) == 1:
            adj_mtx[i + 1][j + 1 + n] = 1

rst = edmonds_karp(adj_mtx, 0, 2*n+1)
if rst == n:
    print('Bob')
else:
    print('Alice')

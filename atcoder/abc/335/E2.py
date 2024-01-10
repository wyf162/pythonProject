# -*- coding : utf-8 -*-
# @Time: 2024/1/6 22:07
# @Author: yefei.wang
# @File: E2.py
import sys, random, bisect
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import permutations
from math import gcd, log

input = lambda: sys.stdin.readline().rstrip()
mi = lambda: map(int, input().split())
li = lambda: list(mi())

N, M = mi()
A = li()
edge = [[] for v in range(N)]
for _ in range(M):
    u, v = mi()
    edge[u - 1].append(v - 1)
    edge[v - 1].append(u - 1)

score = [-1] * N
score[0] = 0

val_to_vs = [[] for a in range(max(A) + 1)]
for i, a in enumerate(A):
    val_to_vs[a].append(i)

det = [False] * N
for a in range(len(val_to_vs)):
    tmp = [v for v in val_to_vs[a] if score[v] != -1]
    tmp.sort(key=lambda v: score[v], reverse=True)
    for v in tmp:
        if det[v]:
            continue
        det[v] = True
        stack = [v]
        while stack:
            v = stack.pop()
            for nv in edge[v]:
                if A[nv] == a and not det[nv]:
                    det[nv] = True
                    score[nv] = score[v]
                    stack.append(nv)
    for v in val_to_vs[a]:
        for nv in edge[v]:
            if A[nv] > A[v]:
                if score[v] != -1:
                    score[nv] = max(score[nv], score[v] + 1)

# print(score)
print(score[-1] + 1)

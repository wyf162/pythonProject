# -*- coding : utf-8 -*-
# @Time: 2024/5/25 10:19
# @Author: yefei.wang
# @File: 894E.py
import math
import sys
from collections import defaultdict
from itertools import accumulate
import bisect

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


def find_SCC(graph, n):
    SCC, S, P = [], [], []
    depth = [0] * n

    stack = list(range(n))
    while stack:
        node = stack.pop()
        if node < 0:
            d = depth[~node] - 1
            if P[-1] > d:
                SCC.append(S[d:])
                del S[d:], P[-1]
                for node in SCC[-1]:
                    depth[node] = -1
        elif depth[node] > 0:
            while P[-1] > depth[node]:
                P.pop()
        elif depth[node] == 0:
            S.append(node)
            P.append(len(S))
            depth[node] = len(S)
            stack.append(~node)
            stack += graph[node]
    return SCC[::-1]


nums1 = list(accumulate([i + 1 for i in range(2 * 10 ** 4 + 5)]))
nums2 = list(accumulate(nums1))


def get_mushroom(w):
    j = bisect.bisect_right(nums1, w)
    if j > 0:
        tot = w * (j + 1) - nums2[j - 1]
    else:
        tot = w
    return tot


def calc_mushroom(w):
    d = int(math.sqrt(w * 2))
    while d * d + d > 2 * w:
        d -= 1
    ret = w * (d + 1) - (d * (d + 1) * (2 * d + 1) // 6 + d * (d + 1) // 2) // 2
    return ret


tcn = 1
for _tcn_ in range(tcn):
    n, m = MI()
    g = [[] for _ in range(n)]
    gw = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = MI()
        u, v = u - 1, v - 1
        g[u].append(v)
        gw[u].append((v, w))

    scc = find_SCC(g, n)
    A = [n for _ in range(n)]
    ng = [defaultdict(int) for _ in range(n)]
    nums = [0 for _ in range(n)]
    for i, sc in enumerate(scc):
        for x in sc:
            A[x] = i

    for x in range(n):
        nx = A[x]
        for y, w in gw[x]:
            ny = A[y]
            if nx == ny:
                nums[nx] += get_mushroom(w)
            else:
                ng[nx][ny] = max(ng[nx][ny], w)

    topo = []
    deg = [0] * n
    father = [[] for _ in range(n)]
    for x in range(n):
        for y in ng[x]:
            deg[y] += 1
            father[y].append(x)

    q = [i for i, d in enumerate(deg) if d == 0]
    topo = []
    while q:
        x = q.pop()
        topo.append(x)
        for y in ng[x]:
            deg[y] -= 1
            if deg[y] == 0:
                q.append(y)

    f = [0] * n
    for x in topo[::-1]:
        f[x] += nums[x]
        for y in father[x]:
            f[y] = max(f[y], f[x] + ng[y][x])
    s = I()
    print(f[A[s-1]])

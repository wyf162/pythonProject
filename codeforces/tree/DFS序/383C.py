# -*- coding: utf-8 -*-
# @Time: 2024/2/29 9:12
# @Author: yfwang
# @File: 383C.py
# https://codeforces.com/problemset/problem/383/C

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n, m = MI()
nums = LI()
g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = GMI()
    g[u].append(v)
    g[v].append(u)

L, R = [-1] * n, [-1] * n
depth = [-1] * n
q = [0]
depth[0] = t = 0
while q:
    u = q[-1]
    if L[u] == -1:
        t += 1
        L[u] = t
        for v in g[u]:
            if depth[v] >= 0:
                continue
            depth[v] = depth[u] + 1
            q.append(v)
    else:
        R[u] = t
        q.pop()

bit = [[0] * (n + 1) for _ in range(2)]


def query(t, x):
    res = 0
    while x:
        res += bit[t][x] - bit[t ^ 1][x]
        x &= x - 1
    return res


def add(t, x, v):
    while x <= n:
        bit[t][x] += v
        x += x & -x


for _ in range(m):
    qry = LI()
    if qry[0] == 1:
        u, v = qry[1] - 1, qry[2]
        add(depth[u] & 1, L[u], v)
        add(depth[u] & 1, R[u] + 1, -v)
    else:
        u = qry[1] - 1
        res = nums[u] + query(depth[u] & 1, L[u])
        print(res)

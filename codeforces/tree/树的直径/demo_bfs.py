# -*- coding: utf-8 -*-
# @Time: 2024/4/19 11:23
# @Author: yfwang
# @File: demo.py.py

#  bfs 求树的直径
import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n = I()
g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = GMI()
    g[u].append(v)
    g[v].append(u)


def bfs(start):
    q = deque([(start, -1)])
    step = -1
    while q:
        step += 1
        for _ in range(len(q)):
            x, fa = q.popleft()
            for y in g[x]:
                if y != fa:
                    q.append((y, x))
    return step, x


# 直径D, 两个端点是v1, v2
_, v1 = bfs(0)
D, v2 = bfs(v1)
print(D, v1, v2)


# -*- coding : utf-8 -*-
# @Time: 2023/10/21 14:04
# @Author: yefei.wang
# @File: d.py

import sys
from collections import deque

# sys.stdin = open('./../../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, m, k = MI()
g = [[] for _ in range(n)]
for _ in range(m):
    u, v, a = MI()
    u -= 1
    v -= 1
    g[u].append([v, a])

q = deque()
q.append((0, 0))

while q:
    x, t = q.popleft()
    for y, a in g[x]:
        if t >= a:
            q.append((y, t + 1))
            if y == n - 1:
                ans = ((t + 1 + k - 1) // k + 1) * k
                exit(print(ans))
print(-1)

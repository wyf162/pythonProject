# -*- coding : utf-8 -*-
# @Time: 2024/4/6 20:11
# @Author: yefei.wang
# @File: D.py

import sys
from heapq import heappush, heappop

input = lambda: sys.stdin.readline().rstrip('\r\n')
sys.stdin = open('./../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
Yn = lambda x: print('Yes' if x else 'No')
mod = 1000000007
mod2 = 998244353

h, w = MI()
grid = [list(input()) for _ in range(h)]
n = I()
mtx = [[-1 for _ in range(w)] for _ in range(h)]

ops = [LI() for _ in range(n)]
for x, y, e in ops:
    x -= 1
    y -= 1
    mtx[x][y] = max(mtx[x][y], e)

si, sj = 0, 0
ti, tj = 0, 0
for i in range(h):
    for j in range(w):
        if grid[i][j] == 'S':
            si, sj = i, j
        if grid[i][j] == 'T':
            ti, tj = i, j

if si == ti and sj == tj:
    exit(print("Yes"))

if mtx[si][sj] <= 0:
    exit(print("No"))

pq = [(-mtx[si][sj], si, sj)]
vis = [[0 for _ in range(w)] for _ in range(h)]
while pq:
    e, x, y = heappop(pq)
    if vis[x][y]:
        continue
    vis[x][y] = 1
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] != '#':
            ne = min(e + 1, -mtx[nx][ny])
            if not vis[nx][ny] and ne <= 0:
                heappush(pq, (ne, nx, ny))
Yn(vis[ti][tj])

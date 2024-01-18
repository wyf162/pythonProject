import sys
from collections import deque

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

h, w = MI()
mtx = [list(input()) for _ in range(h)]
vis = [[0 for j in range(w)] for i in range(h)]

q = deque()
q.append((0, 0))
while q:
    i, j = q.popleft()
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < h and 0 <= nj < w and mtx[i][j] + mtx[ni][nj] in 'snukes':
            if not vis[ni][nj]:
                q.append((ni, nj))
                vis[ni][nj] = 1
    if i == h - 1 and j == w - 1:
        exit(print('Yes'))
print('No')

import sys
from heapq import heappop, heappush
from typing import List

sys.stdin = open('../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
inf = 0x3f3f3f3f3f3f3f

n, a, b, c = MI()
mtx = [LI() for i in range(n)]


def get_shortest_path(dct: List[List[int]], src: int) -> List[int]:
    n = len(dct)
    dis = [inf] * n
    stack = [(0, src)]
    dis[src] = 0

    while stack:
        d, i = heappop(stack)
        if dis[i] < d:
            continue
        for j, w in enumerate(dct[i]):
            dj = w + d
            if dj < dis[j]:
                dis[j] = dj
                heappush(stack, (dj, j))
    return dis


dct1 = [[0 for j in range(n)] for i in range(n)]
dct2 = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        dct1[i][j] = mtx[i][j] * a
        dct2[i][j] = mtx[i][j] * b + c

dist1 = get_shortest_path(dct1, 0)
dist2 = get_shortest_path(dct2, n-1)

rst = min(dist1[-1], dist2[0])
for i in range(1, n-1):
    rst = min(rst, dist1[i]+dist2[i])
print(rst)
import sys
from heapq import heappop, heappush

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 10 ** 9 + 7

N, M = MI()

rst = [0] * N
row = []
for i in range(N):
    heappush(row, i)
ts = []

for _ in range(M):
    t, w, s = MI()
    while ts and ts[0][0] <= t:
        _, x = heappop(ts)
        heappush(row, x)
    if row:
        x = heappop(row)
        rst[x] += w
        heappush(ts, [t+s, x])

for x in rst:
    print(x)

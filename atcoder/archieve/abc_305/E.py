import sys
from heapq import heappop, heappush

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

n, m, k = MI()
g = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = MI()
    g[u].append(v)
    g[v].append(u)

guards = [LI() for _ in range(k)]

vis = [0] * (n + 1)
h = []
for x, d in guards:
    heappush(h, [-d, x])

while h:
    d, x = heappop(h)
    if vis[x]:
        continue
    vis[x] = 1
    if d == 0:
        continue
    for y in g[x]:
        if not vis[y]:
            heappush(h, [d + 1, y])

rst = [i for i, x in enumerate(vis) if x == 1]
print(len(rst))
print(*rst)

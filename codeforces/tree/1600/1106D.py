import sys
from heapq import heappop, heappush

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, m = MI()
g = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = MI()
    g[u].append(v)
    g[v].append(u)

ans = []
vis = [0] * (n + 1)
h = []
heappush(h, 1)
vis[1] = 1
while h:
    x = heappop(h)
    ans.append(x)
    for y in g[x]:
        if not vis[y]:
            heappush(h, y)
            vis[y] = 1


print(' '.join(map(str, ans)))

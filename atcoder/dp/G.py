import sys
from collections import deque

sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(map(int, input().split()))

n, m = MI()

g = [[] for _ in range(n)]
deg = [0] * n
depth = [0] * n
for _ in range(m):
    u, v = GMI()
    deg[v] += 1
    g[u].append(v)

q = deque(i for i, d in enumerate(deg) if d == 0)

while q:
    x = q.popleft()
    for y in g[x]:
        depth[y] = max(depth[y], depth[x] + 1)
        deg[y] -= 1
        if deg[y] == 0:
            q.append(y)
print(max(depth))

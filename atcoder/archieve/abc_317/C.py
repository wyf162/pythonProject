import sys
from collections import deque

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 10 ** 9 + 7

n, m = MI()
g = [[] for i in range(n)]
for _ in range(m):
    u, v, w = MI()
    u -= 1
    v -= 1
    g[u].append([v, w])
    g[v].append([u, w])

ans = 0
for i in range(n):
    q = deque()
    q.append((1 << i, i, 0))

    while q:
        s, x, tmp = q.popleft()
        ans = max(ans, tmp)
        for y, w in g[x]:
            if s >> y & 1:
                continue
            else:
                q.append((s | (1 << y), y, tmp + w))

print(ans)

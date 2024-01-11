import sys
from collections import deque

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, m = MI()
s = input()
g = [[] for _ in range(n)]
deg = [0] * n
for _ in range(m):
    u, v = MI()
    u -= 1
    v -= 1
    g[u].append(v)
    deg[v] += 1

f = [[0] * 26 for _ in range(n)]
q = deque()
for i, d in enumerate(deg):
    if d != 0:
        continue
    q.append(i)
    j = ord(s[i]) - 97
    f[i][j] = 1

size = 0
while q:
    x = q.popleft()
    for y in g[x]:
        for j in range(26):
            f[y][j] = max(f[y][j], f[x][j] + int(ord(s[y]) == j + 97))
        deg[y] -= 1
        if deg[y] == 0:
            q.append(y)
    size += 1

mx = max(max(f[i]) for i in range(n))
# cnt_mx = sum(f[i].count(mx) for i in range(n))
if size < n:
    print(-1)
else:
    print(mx)

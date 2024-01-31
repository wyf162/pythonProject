import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n = I()
g = [[] for _ in range(n)]
deg = [0] * n
for _ in range(n - 1):
    u, v = GMI()
    g[u].append(v)
    g[v].append(u)
    deg[u] += 1
    deg[v] += 1

vis = [0] * n
dep = [0] * n
q = deque()
for i, d in enumerate(deg):
    if d == 1:
        dep[i] = 1
        q.append(i)


while q:
    x = q.popleft()
    for y in g[x]:
        if deg[y] <= 2 and not dep[y]:
            dep[y] = dep[x] + 1
            q.append(y)

rst = set()
mx = max(dep)
for i in range(1, mx+1):
    rst.add((i, n-1-i))
    rst.add((n-1-i, i))
rst = list(rst)
rst.sort()
print(len(rst))
for i in range(len(rst)):
    print(*rst[i])

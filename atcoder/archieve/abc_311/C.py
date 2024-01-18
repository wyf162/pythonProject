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

n = I()
a = LI()

g = [[] for i in range(n)]
deg = [0] * n
for x, y in enumerate(a):
    y -= 1
    deg[y] += 1
    g[x].append(y)

q = deque(i for i, d in enumerate(deg) if d == 0)

while q:
    x = q.popleft()
    for y in g[x]:
        deg[y] -= 1
        if deg[y] == 0:
            q.append(y)

rst = []
for i in range(n):
    if deg[i]:
        while True:
            rst.append(i)
            for j in g[i]:
                if deg[j]:
                    i = j
                    break
            if rst[0] == i:
                break
        break
print(len(rst))
print(*[x+1 for x in rst])



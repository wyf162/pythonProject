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

n, m = MI()

type_number = 3
g = [[] for i in range(type_number)]

for _ in range(n):
    t, x = MI()
    g[t].append(x)

h = []

for x in g[0]:
    heappush(h, x)
    if len(h) > m:
        heappop(h)

ans = sum(h)
g[1].sort(reverse=True)
g[2].sort(reverse=True)
i1 = 0

for i, c in enumerate(g[2]):
    m -= 1
    for _ in range(c):
        if i1<len(g[1]) and g[1][i1] > h[0]:
            heappush(h, g[1][i1])
            i1 += 1
        else:
            break
        while h and len(h) > m:
            heappop(h)

    if h:
        ans = max(ans, sum(h))

    if i1 >= len(g[1]):
        break
print(ans)

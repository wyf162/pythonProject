import bisect
import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    input()
    n, k = MI()
    g = [[] for _ in range(n)]
    deg = [0] * n
    for _ in range(n - 1):
        x, y = GMI()
        g[x].append(y)
        g[y].append(x)
        deg[x] += 1
        deg[y] += 1
    if n == 1:
        if k == 0:
            print(n)
        else:
            print(0)
        continue

    q = deque(i for i, d in enumerate(deg) if d == 1)
    ans = n
    while k and q:
        ans -= len(q)
        for _ in range(len(q)):
            x = q.popleft()
            for y in g[x]:
                deg[y] -= 1
                if deg[y] == 1:
                    q.append(y)
        k -= 1
    print(ans)

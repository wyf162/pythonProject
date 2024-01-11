import sys
from collections import deque

# sys.stdin = open('./../input.txt', 'r')
input = lambda: sys.stdin.readline().rstrip('\r\n')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n, m = MI()
    g = [[] for i in range(1 + n)]
    for _ in range(m):
        a, b, d = MI()
        g[a].append((b, d))
        g[b].append((a, -d))

    f = [None] * (n + 1)
    for i in range(1, n + 1):
        if f[i] is None:
            f[i] = 0
            q = deque()
            q.append(i)
            while len(q):
                u = q.popleft()
                for v, w in g[u]:
                    if f[v] is None:
                        f[v] = f[u] + w
                        q.append(v)
    ans = True
    for u in range(1, n + 1):
        for v, w in g[u]:
            if f[v] != f[u] + w:
                ans = False
                break
        if not ans:
            break
    print(["NO", "YES"][ans])

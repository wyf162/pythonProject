import sys
from collections import deque

# sys.stdin = open('./../input.txt', 'r')
input = lambda: sys.stdin.readline().rstrip('\r\n')

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n, m = MI()
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = MI()
        g[u].append(v)
        g[v].append(u)

    vis = [-1] * (n + 1)
    q = deque()
    q.append(1)
    vis[1] = 1
    while q:
        for _ in range(len(q)):
            x = q.popleft()
            for y in g[x]:
                if vis[y] < 0:
                    vis[y] = vis[x] ^ 1
                    q.append(y)
    ans = [i for i, x in enumerate(vis) if x == 1]
    ans2 = [i for i, x in enumerate(vis) if x == 0]
    if len(ans2) < len(ans):
        ans = ans2
    print(len(ans))
    print(' '.join(map(str, ans)))

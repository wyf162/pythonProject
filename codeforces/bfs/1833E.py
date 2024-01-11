import sys
from collections import deque

sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    a = LGMI()
    g = [set() for _ in range(n)]
    for x, y in enumerate(a):
        g[x].add(y)
        g[y].add(x)

    vis = [0] * n
    circle = chain = 0
    for i in range(n):
        if vis[i]:
            continue


        def bfs(x):
            q = deque()
            q.append(x)
            vis[x] = 1
            tot = 0
            cnt = 0
            while q:
                x = q.popleft()
                tot += len(g[x])
                cnt += 1
                for y in g[x]:
                    if not vis[y]:
                        q.append(y)
                        vis[y] = 1

            if tot == cnt * 2 and tot > 4:
                return 'circle'
            else:
                return 'chain'


        ret = bfs(i)
        if ret == 'circle':
            circle += 1
        else:
            chain += 1

    mx = circle + chain
    mi = circle + (1 if chain else 0)
    print(mi, mx)

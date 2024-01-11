import sys
from collections import deque

# sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

# mad city

tcn = I()
for _ in range(tcn):
    n, a, b = MI()
    edges = [LI() for i in range(n)]
    if a == b:
        print('NO')
        continue

    g = [[] for i in range(n + 1)]
    deg = [0 for i in range(n + 1)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
        deg[u] += 1
        deg[v] += 1

    q = deque()
    for i in range(1, n + 1):
        if deg[i] == 1:
            q.append(i)
    vis = [0 for i in range(n + 1)]
    k = 1
    while q:
        for i in range(len(q)):
            x = q.popleft()
            vis[x] = k
            for y in g[x]:
                deg[y] -= 1
                if deg[y] == 1 and vis[y] == 0:
                    q.append(y)
        k += 1
    # if vis[b] == 0:
    #     print('YES')
    #     continue
    #
    # if 0 < vis[b] < vis[a]:
    #     print('YES')
    #     continue

    db = 0
    q = deque()
    q.append(b)
    find_ring = False
    while True:
        for i in range(len(q)):
            x = q.popleft()
            if vis[x] == 0:
                node = x
                find_ring = True
                break
            for y in g[x]:
                q.append(y)
        if find_ring:
            break
        db += 1

    dx = 0
    q = deque()
    q.append(a)
    find_ring = False
    bvis = [True for i in range(n + 1)]
    bvis[a] = False
    while True:
        for i in range(len(q)):
            x = q.popleft()
            if x == node:
                find_ring = True
                break
            for y in g[x] and bvis[y]:
                q.append(y)
                bvis[y] = False
        if find_ring:
            break
        dx += 1

    if db == 0 or db < dx:
        print('YES')
    else:
        print('NO')

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
    n, k = MI()
    a = LI()
    marked = [0] * n
    for x in a:
        x -= 1
        marked[x] = 1

    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = GMI()
        g[u].append(v)
        g[v].append(u)


    def bfs(start):
        q = deque([(start, -1)])
        step = 0
        mx, mv = 0, start
        while q:
            step += 1
            for _ in range(len(q)):
                x, fa = q.popleft()
                for y in g[x]:
                    if y != fa:
                        q.append((y, x))
                        if marked[y]:
                            if step > mx:
                                mx, mv = step, y
        return mx, mv


    mx1, v1 = bfs(a[0] - 1)
    mx2, v2 = bfs(v1)
    # print(v1, v2, mx1, mx2)
    ans = (mx2 + 1) // 2
    print(ans)

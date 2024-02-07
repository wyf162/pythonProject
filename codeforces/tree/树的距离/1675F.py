import bisect
import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
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
    x0, y0 = GMI()
    A = LGMI()
    edges = [LGMI() for _ in range(n-1)]

    vis = [0] * n
    for i in A + [x0, y0]:
        vis[i] = 1

    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)

    dep = [-1] * n
    dep[x0] = 0
    stk = [[x0, -1, 0]]
    while stk:
        x, fa, t = stk.pop()
        if t == 0:
            for y in g[x]:
                if dep[y] == -1:
                    dep[y] = dep[x] + 1
                    stk.append([y, x, 1])
                    stk.append([y, x, 0])
        else:
            vis[fa] |= vis[x]
    ans = 2 * (sum(vis) - 1) - dep[y0]
    print(ans)

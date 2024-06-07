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
    X = LGMI()
    edges = [LGMI() for _ in range(n - 1)]

    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)

    leafs = [len(g[i]) == 1 for i in range(n)]
    leafs[0] = False

    ans = False
    xr = [0]
    vis = [0] * n
    vis[0] = 2
    ts = 0

    while xr:
        Y = []
        for x in X:
            vis[x] = 1
            for y in g[x]:
                if vis[y] != 1:
                    vis[y] = 1
                    Y.append(y)
        X = Y

        nxr = []
        for x in xr:
            for y in g[x]:
                if leafs[y] and vis[y] != 1:
                    ans = True
                    break
                if vis[y] == 0:
                    nxr.append(y)
                    vis[y] = 2
            if ans:
                break
        if ans:
            break
        xr = nxr
    YN(ans)

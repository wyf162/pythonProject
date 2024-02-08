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
    n = I()
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = GMI()
        g[u].append(v)
        g[v].append(u)

    fa = [-1] * n
    dfs = []
    stk = [0]
    fa[0] = n

    while stk:
        x = stk.pop()
        dfs.append(x)
        for y in g[x]:
            if fa[y] == -1:
                fa[y] = x
                stk.append(y)
    fa[0] = -1
    # print(dfs)

    size = [0] * n
    for x in dfs[::-1]:
        size[x] += 1
        if fa[x] >= 0:
            size[fa[x]] += size[x]
    # print(size)

    centroid = []
    mx_size = n

    for x in dfs[::-1]:
        mx = 1
        tot = 0
        for y in g[x]:
            if y == fa[x]:
                continue
            mx = max(mx, size[y])
            tot += size[y]
        mx = max(mx, n - tot - 1)
        if mx == mx_size:
            centroid.append(x)
        elif mx < mx_size:
            mx_size = mx
            centroid = [x]
    if len(centroid) == 1:
        print(1, g[0][0] + 1)
        print(1, g[0][0] + 1)
    else:
        # print(centroid)
        v1, v2 = centroid[0], centroid[1]
        vx, fax = v1, fa[v1]
        while True:
            for vy in g[vx]:
                if vy != fax:
                    fax = vx
                    vx = vy
                    break
            else:
                break
        print(vx+1, fax+1)
        print(vx+1, v2+1)

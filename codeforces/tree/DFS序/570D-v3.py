import math
import bisect
import sys

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))


class RMQ:
    def __init__(self, init):
        self.N = len(init)
        self.LOGN = int(math.log2(self.N) + 1)
        self.f = [[0] * self.N for _ in range(self.LOGN)]
        for i in range(self.N):
            self.f[0][i] = init[i]
        for i in range(1, self.LOGN):
            for j in range(self.N - (1 << i) + 1):
                self.f[i][j] = self.f[i - 1][j] ^ self.f[i - 1][j + (1 << (i - 1))]

    def query(self, l, r):
        k = int(math.log2(r - l))
        return self.f[k][l] ^ self.f[k][r - (1 << k)]


N = 500005
G = [[] for _ in range(N)]
val = [[] for _ in range(N)]
dfsQ = [[] for _ in range(N)]
w = [0] * N
dfn = [0] * N
dep = [0] * N
Siv = [0] * N
MaxDpt = 0
res = [None] * N
Len = [0] * N


def dfs(u, fa=0, dpt=1):
    global MaxDpt
    MaxDpt = max(MaxDpt, dpt)
    dfn[u] = dfn[0] + 1
    dfn[0] = dfn[0] + 1
    dep[u] = dpt
    Siv[u] = 1
    val[dpt].append(w[u])
    dfsQ[dpt].append(dfn[u])
    for v in G[u]:
        if v == fa:
            continue
        dfs(v, u, dpt + 1)
        Siv[u] += Siv[v]


def main():
    global MaxDpt
    global G, val, dfsQ, w, dfn, dep, Siv, res
    n, q = map(int, input().split())
    for i in range(N):
        G[i] = []
        val[i] = []
        dfsQ[i] = []

    fa = LI()
    for i in range(n - 1):
        u, v = i + 2, fa[i]
        G[u].append(v)
        G[v].append(u)
    w = [0] + [1 << (ord(c) - 97) for c in input()]
    dfs(1)
    for i in range(1, MaxDpt + 1):
        res[i] = RMQ(val[i])
        Len[i] = len(val[i])

    for _ in range(q):
        x, k = map(int, input().split())
        l = bisect.bisect(dfsQ[k], dfn[x], 0, Len[k])
        r = bisect.bisect(dfsQ[k], dfn[x] + Siv[x], 0, Len[k])

        if r - l <= 0:
            print('Yes')
            continue
        rst = res[k].query(l, r)
        if rst & (rst - 1):
            print('No')
        else:
            print('Yes')


if __name__ == "__main__":
    import sys

    sys.stdin = open('../../input.txt', 'r')
    sys.setrecursionlimit(51000)
    main()

import sys
from collections import Counter
from heapq import heappop, heappush
from types import GeneratorType


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


input = lambda: sys.stdin.readline().rstrip('\r\n')
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
    n = I()
    success = True
    g = [[] for _ in range(n)]
    fa = [_ for _ in range(n * 2)]


    def find(x):
        r = x
        while r != fa[r]:
            r = fa[r]

        k = x
        while k != r:
            fa[k], k = r, fa[k]
        return fa[x]


    def union(x, y):
        fx = find(x)
        fy = find(y)
        if fx < fy:
            fa[fy] = fx
        else:
            fa[fx] = fy


    for i in range(n):
        x, y = GMI()
        if x == y:
            success = False
        if len(g[x]) >= 2 or len(g[y]) >= 2:
            success = False
        if len(g[x]) and len(g[y]):
            fx = find(g[x][0])
            fy = find(g[y][0] + n)
            if fx == fy:
                success = False
        if len(g[x]):
            union(i, g[x][0] + n)
            union(i + n, g[x][0])
        if len(g[y]):
            union(i, g[y][0] + n)
            union(i + n, g[y][0])
        g[x].append(i)
        g[y].append(i)
    YN(success)

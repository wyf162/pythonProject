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
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = GMI()
        g[u].append(v)
        g[v].append(u)

    sz = [0] * n
    f = [0] * n


    @bootstrap
    def dfs(x, fa):
        sz[x] = 1
        s1 = s2 = -1
        for y in g[x]:
            if y != fa:
                yield dfs(y, x)
                sz[x] += sz[y]
                if s1 == -1:
                    s1 = y
                elif s2 == -1:
                    s2 = y
        if s1 == -1:
            f[x] = 0
        elif s2 == -1:
            f[x] = sz[s1] - 1
        else:
            f[x] = max(sz[s1] - 1 + f[s2], sz[s2] - 1 + f[s1])
        yield


    dfs(0, -1)
    ans = f[0]
    print(ans)

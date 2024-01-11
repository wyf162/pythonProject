import sys
from types import GeneratorType

BUFSIZE = 8192


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


sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())

tcn = I()
for _tcn_ in range(tcn):
    n, k, c = MI()
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = GMI()
        g[u].append(v)
        g[v].append(u)

    depth = [0] * n


    @bootstrap
    def dfs1(x, fa):
        for y in g[x]:
            if y != fa:
                yield dfs1(y, x)
                depth[y] = depth[x] + 1
        yield


    dfs1(0, -1)
    print(depth)

    down1 = [0] * n
    down2 = [0] * n


    @bootstrap
    def dfs2(x, fa):
        ret = []
        for y in g[x]:
            if y != fa:
                yield dfs2(y, x)
                ret.append(down1[y] + 1)
                ret.append(down2[y] + 1)
        ret.sort()
        down1[x] = ret[-1] if len(ret) > 0 else 0
        down2[x] = ret[-2] if len(ret) > 1 else 0
        yield


    dfs2(0, -1)
    print(down1)
    print(down2)

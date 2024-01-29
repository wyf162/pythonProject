import sys
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


# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n, a, b = MI()
    g = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        u, v, w = MI()
        g[u].append((v, w))
        g[v].append((u, w))

    vis = set()


    @bootstrap
    def dfs(x, fa, xor):
        if x == b:
            yield
        vis.add(xor)
        for y, w in g[x]:
            if y != fa:
                yield dfs(y, x, xor ^ w)
        yield


    dfs(a, 0, 0)
    ans = False


    @bootstrap
    def dfs2(x, fa, xor):
        if x != b and xor in vis:
            global ans
            ans = True
            yield
        for y, w in g[x]:
            if y != fa:
                yield dfs2(y, x, xor ^ w)
        yield


    dfs2(b, 0, 0)

    if ans:
        print('YES')
    else:
        print('NO')

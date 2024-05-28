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


input = lambda: sys.stdin.readline().rstrip('\r\n')

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(map(int, input().split()))
mod = 10 ** 9 + 7

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = GMI()
        g[u].append(v)
        g[v].append(u)

    size = [0] * n


    @bootstrap
    def dfs(x, fa):
        c = 0
        for y in g[x]:
            if y != fa:
                yield dfs(y, x)
                size[x] += size[y]
                c += 1
        if c == 0:
            size[x] = 1
        yield


    dfs(0, -1)
    # print(size)

    q = I()
    for _ in range(q):
        x, y = GMI()
        rst = size[x] * size[y]
        print(rst)

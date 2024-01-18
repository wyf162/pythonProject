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


sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

n = I()
g = [[] for i in range(n)]
for i in range(n - 1):
    u, v = GMI()
    g[u].append(v)
    g[v].append(u)

size = [0] * n


@bootstrap
def dfs(x, fa):
    size[x] = 1
    for y in g[x]:
        if y != fa:
            yield dfs(y, x)
            size[x] += size[y]
    yield


dfs(0, -1)
# print(size)
ans = 0


@bootstrap
def dfs2(x, fa):
    a = n - size[x]
    b = 0
    c = 0
    for y in g[x]:
        if y != fa:
            global ans
            ans += a * b * size[y]
            ans += c * size[y]
            c += size[y] * b
            b += size[y]

            yield dfs2(y, x)
    yield


dfs2(0, -1)

print(ans)

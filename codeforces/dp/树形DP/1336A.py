import sys
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


# sys.setrecursionlimit(10 ** 6 + 5)
# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(map(int, input().split()))
mod = 10 ** 9 + 7

n, k = MI()
g = [[] for _ in range(n)]
for _ in range(n - 1):
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
h = []
heappush(h, (-size[0], 0))
ans = 0
hst = dict()
hst[0] = 1

while k < n:
    sz, x = heappop(h)
    ans += size[x] - hst[x]
    for y in g[x]:
        if y not in hst:
            hst[y] = hst[x] + 1
            heappush(h, (hst[y] - size[y], y))
    k += 1

print(ans)

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
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
g = [[] for _ in range(n)]
for i in range(n - 1):
    u, v = GMI()
    g[u].append(v)
    g[v].append(u)

tree = [[] for _ in range(n)]


@bootstrap
def dfs(x, fa):
    for y in g[x]:
        if y == fa:
            continue
        tree[x].append(y)
        yield dfs(y, x)
    yield


dfs(0, -1)

dp = [0] * n


@bootstrap
def dfs2(x):
    if tree[x]:
        for y in tree[x]:
            yield dfs2(y)
            dp[x] += dp[y]
        dp[x] /= len(tree[x])
        dp[x] += 1
    yield


dfs2(0)
# print(dp)
print(format(dp[0], '.15f'))

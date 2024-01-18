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
mod = 10 ** 9 + 7

n = I()
g = [[] for i in range(n)]
for i in range(n):
    tmp = LGMI()
    g[i] = tmp[1:]

vis = set()
seq = []


@bootstrap
def dfs(x):
    for y in g[x]:
        if y not in vis:
            vis.add(y)
            yield dfs(y)
    seq.append(x + 1)

    yield


dfs(0)
print(' '.join(map(str, seq[:-1])))

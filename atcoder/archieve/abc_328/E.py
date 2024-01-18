import sys
import time
from types import GeneratorType

# t1 = time.time()


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


# sys.stdin = open('./../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())

N, M, K = MI()
g = [[] for _ in range(N)]
for i in range(M):
    u, v, w = MI()
    u, v = u - 1, v - 1
    g[u].append([v, w, i])
    g[v].append([u, w, i])

ans = K


def check(rst):
    s = 0
    q = [0]
    vis = set()
    while q:
        x = q.pop()
        vis.add(x)
        for y, w, b in g[x]:
            if rst >> b & 1 and y not in vis:
                q.append(y)
                s += w
                s %= K
    if len(vis) == N:
        global ans
        ans = min(ans, s)


@bootstrap
def perm(b, m, rst):
    if m == 0:
        yield check(rst)
    for i in range(b, M):
        if M - i - 1 < m - 1:
            yield
        yield perm(i + 1, m - 1, rst | (1 << i))
    yield


perm(0, N - 1, 0)
print(ans)

# t2 = time.time()
# print(f"{t2 - t1}s")

# -*- coding : utf-8 -*-
# @Time: 2024/1/28 19:42
# @Author: yefei.wang
# @File: E.py

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


input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n = I()
g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = GMI()
    g[u].append(v)
    g[v].append(u)

dp1 = [1] * n
dp2 = [1] * n


@bootstrap
def dfs(x, fa):
    for y in g[x]:
        if y == fa:
            continue
        yield dfs(y, x)
        dp1[x] *= dp2[y]
        dp2[x] *= (dp1[y] + dp2[y])
        dp1[x] %= mod
        dp2[x] %= mod
    yield


dfs(0, -1)

rst = (dp1[0] + dp2[0]) % mod
print(rst)

# -*- coding: utf-8 -*-
# @Time: 2024/5/28 16:49
# @Author: yfwang
# @File: 1083A.py

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


import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n = I()
nums = LI()

g = [[] for _ in range(n)]
for i in range(n - 1):
    u, v, w = GMI()
    w += 1
    g[u].append((v, w))
    g[v].append((u, w))

cache = dict()

ans = 0


@bootstrap
def dfs(x, fa):
    if (x, fa) in cache:
        yield cache[(x, fa)]
    rets1 = []
    for y, w in g[x]:
        if y == fa:
            continue
        rets1.append(next(dfs(y, x)) - w + nums[x])

    rets1.sort(reverse=True)
    global ans
    if len(rets1) == 0:
        ans = max(nums[x], ans)
    if len(rets1) >= 1:
        ans = max(rets1[0], ans)
    if len(rets1) >= 2:
        ans = max(ans, rets1[0] + rets1[1] - nums[x])

    if rets1:
        ret = max(rets1[0], nums[x])
    else:
        ret = nums[x]
    cache[(x, fa)] = ret
    yield ret


dfs(0, -1)
print(ans)

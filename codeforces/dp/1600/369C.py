# -*- coding : utf-8 -*-
# @Time: 2024/1/11 21:12
# @Author: yefei.wang
# @File: 369C.py
# https://codeforces.com/problemset/problem/219/D
# trees

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

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

n = I()
g = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v, w = MI()
    g[u].append([v, w])
    g[v].append([u, w])

# dp1 标识下面有孩子被选过，不用再选
dp1 = [0 for i in range(n + 1)]
# dp2 标识选择该点
dp2 = [0 for i in range(n + 1)]


@bootstrap
def dfs(x, fa, tag):
    if tag == 2:
        dp2[x] = 1
    for y, w in g[x]:
        if y != fa:
            yield dfs(y, x, w)
            if dp2[y] or dp1[y]:
                dp2[x] = 0
                dp1[x] = 1
    yield


dfs(1, 0, 0)

rst = [i for i, x in enumerate(dp2) if x == 1]
print(len(rst))
print(*rst)

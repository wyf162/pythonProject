# -*- coding : utf-8 -*-
# @Time: 2023/12/8 19:15
# @Author: yefei.wang
# @File: C.py

from functools import lru_cache
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


class TreeMaxDist:

    def __init__(self, n, edegs):
        self.n = n
        self.edges = edegs

    def tree_max_dist(self):

        deg = [0] * self.n
        for u, v in self.edges:
            deg[u] += 1
            deg[v] += 1
        q = [i for i, d in enumerate(deg) if d == 1]
        dist = [0] * self.n

        g = [[] for i in range(self.n)]
        for u, v in self.edges:
            g[u].append(v)
            g[v].append(u)

        depth = [0] * self.n
        B = 21
        father = [[0] * B for i in range(self.n)]

        @bootstrap
        def dfs(x, fa, dep):
            depth[x] = dep
            father[x][0] = fa
            for y in g[x]:
                if y != fa:
                    yield dfs(y, x, dep + 1)
            yield

        dfs(0, -1, 0)

        for i in range(1, B):
            for x in range(self.n):
                father[x][i] = father[father[x][i - 1]][i - 1]

        @lru_cache(None)
        def get_lca(x, y):
            # 令depth[y] > depth[x]
            if depth[x] > depth[y]:
                x, y = y, x
            tmp = depth[y] - depth[x]
            for j in range(B):
                if tmp >> j & 1:
                    y = father[y][j]
            if y == x:
                return x

            for j in range(B - 1, -1, -1):
                px, py = father[x][j], father[y][j]
                if px != py:
                    x, y = px, py
            return father[x][0]

        for u in range(self.n):
            for v in q:
                lca = get_lca(u, v)
                depth_u = depth[u]
                depth_v = depth[v]
                depth_lca = depth[lca]
                dist[u] = max(dist[u], depth_u + depth_v - 2 * depth_lca)
        return sum(dist)


class TreePathSum:

    def __init__(self, n, edges):
        # starts with 0
        self.edges = edges
        self.n = n

    def tree_path_sum(self):
        tree = [[] for _ in range(self.n)]
        for u, v in self.edges:
            tree[u].append(v)
            tree[v].append(u)
        s = [0] * self.n
        dp = [0] * self.n

        @bootstrap
        def dfs(x, fa):
            s[x] = 1
            for y in tree[x]:
                if y != fa:
                    yield dfs(y, x)
                    s[x] += s[y]
                    dp[x] += dp[y] + (self.n - s[y]) * s[y]
            yield

        dfs(0, -1)
        return dp[0]


import sys

sys.stdin = open('../../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

n, m = MI()

edges1 = []
edges2 = []
for _ in range(n + m - 2):
    u, v = MI()
    if 1 <= u <= n:
        u -= 1
        v -= 1
        edges1.append([u, v])
    else:
        u -= n + 1
        v -= n + 1
        edges2.append([u, v])

d1 = TreeMaxDist(n, edges1).tree_max_dist()
# d1 = 19
d2 = TreeMaxDist(m, edges2).tree_max_dist()

s1 = TreePathSum(n, edges1).tree_path_sum()
s2 = TreePathSum(m, edges2).tree_path_sum()
rst = s1 + s2 + d1 * m + d2 * n + n * m
print(rst)

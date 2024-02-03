# -*- coding : utf-8 -*-
# @Time: 2024/2/3 19:09
# @Author: yefei.wang
# @File: 1805D.py

import sys
from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.cnt = n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        self.cnt -= 1
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members


input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
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
for i in range(n - 1):
    u, v = GMI()
    g[u].append(v)
    g[v].append(u)


def dfs(root):
    dist = [-1] * n
    todo = [root]
    dist[root] = 0
    while todo:
        v = todo.pop()
        for u in g[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + 1
                todo.append(u)
    mx = max(dist)
    v = dist.index(mx)
    return mx, v, dist


_, v0, _ = dfs(0)
_, v1, dist0 = dfs(v0)
_, _, dist1 = dfs(v1)

edgew = [[] for i in range(n + 1)]
for i in range(n):
    if i != v0:
        edgew[dist0[i]].append((i, v0))
    if i != v1:
        edgew[dist1[i]].append((i, v1))

uf = UnionFind(n)
ans = [0] * n
for k in range(n, 0, -1):
    for x, y in edgew[k]:
        uf.union(x, y)
    ans[k - 1] = uf.cnt

print(*ans)

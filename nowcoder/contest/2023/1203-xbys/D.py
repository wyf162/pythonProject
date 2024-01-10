# -*- coding : utf-8 -*-
# @Time: 2023/12/3 20:13
# @Author: yefei.wang
# @File: D.py
import sys
from collections import defaultdict
from heapq import heappop, heappush
from math import inf
from typing import DefaultDict, List


class UnionFind:
    def __init__(self, n: int) -> None:
        self.root = [i for i in range(n)]
        self.size = [1] * n
        self.part = n
        return

    def find(self, x):
        lst = []
        while x != self.root[x]:
            lst.append(x)
            # merge to the direct root node after query
            x = self.root[x]
        for w in lst:
            self.root[w] = x
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        if self.size[root_x] >= self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.root[root_x] = root_y
        self.size[root_y] += self.size[root_x]
        # assign the rank of non-root nodes to 0
        self.size[root_x] = 0
        self.part -= 1
        return True

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def get_root_part(self):
        # get the nodes list of every root
        part = defaultdict(list)
        n = len(self.root)
        for i in range(n):
            part[self.find(i)].append(i)
        return part

    def get_root_size(self) -> DefaultDict[int, int]:
        # get the size of every root
        size = defaultdict(int)
        n = len(self.root)
        for i in range(n):
            size[self.find(i)] = self.size[self.find(i)]
        return size


class MinimumSpanningTree:
    def __init__(self, edges, n, method="kruskal"):
        self.n = n
        self.edges = edges
        self.cost = 0
        self.cnt = 0
        self.gen_minimum_spanning_tree(method)
        return

    def gen_minimum_spanning_tree(self, method):

        if method == "kruskal":
            # Edge priority
            self.edges.sort(key=lambda item: item[2])
            # greedy selection of edges based on weight for connected merging
            uf = UnionFind(self.n)
            for x, y, z in self.edges:
                if uf.union(x, y):
                    self.cost += z
            if uf.part != 1:
                self.cost = -1
        else:
            # Point priority with Dijkstra
            dct = [dict() for _ in range(self.n)]
            for i, j, w in self.edges:
                c = dct[i].get(j, float("inf"))
                c = c if c < w else w
                dct[i][j] = dct[j][i] = c
            dis = [inf] * self.n
            dis[0] = 0
            visit = [0] * self.n
            stack = [[0, 0]]
            while stack:
                d, i = heappop(stack)
                if visit[i]:
                    continue
                visit[i] = 1
                # cost of mst
                self.cost += d
                # number of connected node
                self.cnt += 1
                for j in dct[i]:
                    w = dct[i][j]
                    if w < dis[j]:
                        dis[j] = w
                        heappush(stack, [w, j])
        return


sys.stdin = open('../../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353


def get_zero(x, y):
    z = x * y
    c = 0
    while True:
        if z % 10 == 0:
            c += 1
            z //= 10
        else:
            break
    return c


n, m = MI()
a = LI()
edges = []
tot = 0
for _ in range(m):
    u, v = GMI()
    w = get_zero(a[u], a[v])
    tot += w
    edges.append((u, v, w))

mst = MinimumSpanningTree(edges, n)
rst = tot - mst.cost
print(rst)

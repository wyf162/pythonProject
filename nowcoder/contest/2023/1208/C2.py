# -*- coding : utf-8 -*-
# @Time: 2023/12/8 19:29
# @Author: yefei.wang
# @File: C2.py

import math

from collections import deque
from typing import List
from math import inf


class TreeAncestor:

    def __init__(self, edges: List[List[int]]):
        n = len(edges)
        self.parent = [-1] * n
        self.depth = [-1] * n
        stack = deque([0])
        self.depth[0] = 0
        while stack:
            i = stack.popleft()
            for j in edges[i]:
                if self.depth[j] == -1:
                    self.depth[j] = self.depth[i] + 1
                    self.parent[j] = i
                    stack.append(j)

        self.cols = max(2, math.ceil(math.log2(n)))
        self.dp = [[-1] * self.cols for _ in range(n)]
        for i in range(n):
            self.dp[i][0] = self.parent[i]

        for j in range(1, self.cols):
            for i in range(n):
                father = self.dp[i][j - 1]
                if father != -1:
                    self.dp[i][j] = self.dp[father][j - 1]
        return

    def get_kth_ancestor(self, node: int, k: int) -> int:
        for i in range(self.cols - 1, -1, -1):
            if k & (1 << i):
                node = self.dp[node][i]
                if node == -1:
                    break
        return node

    def get_lca(self, x: int, y: int) -> int:
        if self.depth[x] < self.depth[y]:
            x, y = y, x
        while self.depth[x] > self.depth[y]:
            d = self.depth[x] - self.depth[y]
            x = self.dp[x][int(math.log2(d))]
        if x == y:
            return x
        for k in range(int(math.log2(self.depth[x])), -1, -1):
            if self.dp[x][k] != self.dp[y][k]:
                x = self.dp[x][k]
                y = self.dp[y][k]
        return self.dp[x][0]

    def get_dist(self, u: int, v: int) -> int:
        lca = self.get_lca(u, v)
        depth_u = self.depth[u]
        depth_v = self.depth[v]
        depth_lca = self.depth[lca]
        return depth_u + depth_v - 2 * depth_lca


class TreeMaxDist:

    def __init__(self, n, edegs):
        self.n = n
        self.edges = edegs

    def tree_max_dist(self):

        deg = [] * self.n
        for u, v in self.edges:
            deg[u] += 1
            deg[v] += 1

        q = [i for i, d in enumerate(deg) if d == 1]
        dist = [0] * self.n
        ta = TreeAncestor(self.edges)
        for i in range(self.n):
            for j in q:
                dist[i] = max(dist[i], ta.get_dist(i, j))
        return sum(dist)
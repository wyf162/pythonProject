# -*- coding : utf-8 -*-
# @Time: 2023/12/8 19:35
# @Author: yefei.wang
# @File: C3.py

from collections import defaultdict


class TreePathSum:

    def __init__(self, n, edges):
        # starts with 0
        self.edges = edges
        self.n = n

    def tree_path_sum(self,):
        tree = [[] for _ in range(self.n)]
        for u, v in self.edges:
            tree[u].append(v)
            tree[v].append(u)

        s = [0] * self.n
        dp = [0] * self.n

        def dfs(x, fa):
            s[x] = 1
            for y in tree[x]:
                if y !=fa:
                    dfs(y, x)
                    s[x] += s[y]
                    dp[x] += dp[y] + (self.n - s[y]) * s[y]

        dfs(0, -1)
        return dp[0]


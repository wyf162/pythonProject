# -*- coding : utf-8 -*-
# @Time: 2023/9/17 17:12
# @Author: yefei.wang
# @File: 2685_countCompleteComponents.py
from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[v].append(u)
            g[u].append(v)

        unvis = [True for _ in range(n)]

        def dfs(x, group_tag):
            for y in g[x]:
                if unvis[y]:
                    dfs(y, group_tag)
                    unvis[y] = False
        tag = 0
        for i in range(n):
            if unvis[i]:
                dfs(i, tag)
                tag += 1
        
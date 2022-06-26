# -*- coding : utf-8 -*-
# @Time: 2022/6/26 19:03
# @Author: yefei.wang
# @File: 6106_count_pairs.py
import collections
from itertools import accumulate
from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        # 查：寻找x的祖先节点
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        # 并：将x的祖先节点挂到y的祖先节点上
        def union(x, y):
            parent[find(x)] = find(y)

        parent = list(range(n))  # 初始化每个节点的祖先节点为其自身
        for u, v in edges:
            union(u, v)  # 并

        for i in range(n):  # 统一祖先节点：一个连通块压缩为一个点
            parent[i] = find(i)

        vals = list(collections.Counter(parent).values())  # 每个连通块的大小
        presum = list(accumulate(vals))  # 连通块大小的前缀和
        ans = 0
        for i in range(len(vals)):
            ans += vals[i] * (n - presum[i])  # 数学关系

        return ans
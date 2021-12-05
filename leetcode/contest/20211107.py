# _*_ coding: utf-8 _*_
# @Time : 2021/11/7 上午11:31 
# @Author : wangyefei
# @File : 20211107.py
import math
from copy import deepcopy
from functools import lru_cache
from typing import List


class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        dp = [0] * n
        if word[0] in "aeiou": dp[0] = 1
        for i in range(1, n):
            if word[i] in "aeiou":
                dp[i] = dp[i - 1] + i + 1
            else:
                dp[i] = dp[i - 1]
        return sum(dp)

    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l = 1
        r = int(1e5 + 1)
        while l < r:
            m = (l + r) >> 1
            print(l, r, m)
            if self.check(n, quantities, m):
                r = m
            else:
                l = m + 1
        return l

    def check(self, n, qs, k):
        c = 0
        for q in qs:
            c += math.ceil(q / k)
        return c <= n

    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        hst = {}
        hst_time = {}
        for edge in edges:
            hst[edge[0]] = hst.get(edge[0], [])
            hst[edge[0]].append(edge[1])
            hst[edge[1]] = hst.get(edge[1], [])
            hst[edge[1]].append(edge[0])
            hst_time[(edge[0], edge[1])] = edge[2]
            hst_time[(edge[1], edge[0])] = edge[2]
        print(hst)
        print(hst_time)

        start_node = Node(0, maxTime, {0})
        q = [start_node]
        ans = values[0]
        while q:
            node = q.pop(0)
            cur = node.cur
            for nex in hst.get(cur, []):
                new_time = node.time - hst_time[(cur, nex)]
                if new_time >= 0:
                    new_set = deepcopy(node.val)
                    new_set.add(nex)
                    new_node = Node(nex, new_time, new_set)
                    if nex==0:
                        ans = max(ans, new_node.compute(values))
                    q.append(new_node)
        return ans


class Node(object):
    def __init__(self, cur, time, val):
        self.cur = cur
        self.time = time
        self.val = val

    def compute(self, vals):
        ans = 0
        print(self.val)
        for v in self.val:
            ans += vals[v]
        return ans


if __name__ == "__main__":
    values = [5, 10, 15, 20]
    edges = [[0, 1, 10], [1, 2, 10], [0, 3, 10]]
    maxTime = 30
    sol = Solution()
    ans = sol.maximalPathQuality(values, edges, maxTime)
    print(ans)


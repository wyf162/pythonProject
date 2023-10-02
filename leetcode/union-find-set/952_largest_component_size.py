# -*- coding : utf-8 -*-
# @Time: 2022/7/30 15:33
# @Author: yefei.wang
# @File: 952_largest_component_size.py
from typing import List
from collections import Counter


class UnionFind:

    def __init__(self, n: int) -> None:
        self.parent = [_ for _ in range(n)]
        self.rank = [1 for _ in range(n)]

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[px] = py
        self.rank[px] += self.rank[py]


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        uf = UnionFind(max(nums) + 1)
        for num in nums:
            i = 2
            while i * i <= num:
                if num % i == 0:
                    uf.merge(num, i)
                    uf.merge(num, num // i)
                i += 1
        return max(Counter(uf.find(num) for num in nums).values())


if __name__ == '__main__':
    sol = Solution()
    nums = [4, 6, 15, 35]
    ret = sol.largestComponentSize(nums)
    print(ret)

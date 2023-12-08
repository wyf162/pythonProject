# -*- coding : utf-8 -*-
# @Time: 2023/11/26 10:41
# @Author: yefei.wang
# @File: C.py
from collections import defaultdict
from typing import List


class UnionFind:

    def __init__(self, n: int):
        self.parent = [_ for _ in range(n)]
        self.size = [1 for _ in range(n)]
        self.group = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_x] = root_y
        self.size[root_y] += self.size[root_x]
        self.group -= 1
        return True


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        uf = UnionFind(n)
        xi = [[x, i] for i, x in enumerate(nums)]
        xi.sort()
        for i in range(1, n):
            if xi[i][0] - xi[i - 1][0] <= limit:
                uf.merge(xi[i][1], xi[i - 1][1])

        group = defaultdict(list)
        for i in range(n):
            fa = uf.find(i)
            group[fa].append(nums[i])
        for k, v in group.items():
            group[k].sort(reverse=True)
        ans = []
        for i in range(n):
            fa = uf.find(i)
            x = group[fa].pop()
            ans.append(x)
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 5, 3, 9, 8]
    limit = 2
    ret = sol.lexicographicallySmallestArray(nums, limit)
    print(ret)

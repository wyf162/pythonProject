# _*_ coding: utf-8 _*_
# @Time : 2022/08/13 12:38 PM 
# @Author : yefe
# @File : 2003_smallest_missing_value_subtree
from typing import List
from collections import deque, defaultdict


class UnionFind:

    def __init__(self, n: int):
        self.parent = [_ for _ in range(n)]
        self.rank = [0 for _ in range(n)]
        self.count = n

    def find(self, x: int) -> int:

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if self.rank[root_x] > self.rank[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_x] = root_y
        self.rank[root_y] += self.rank[root_x]
        self.count -= 1


class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        n = len(nums)
        g = [[] for _ in range(n)]
        for u, v in enumerate(parents):
            if v >= 0:
                g[v].append(u)

        uf = UnionFind(100002)
        ans = [0] * n

        def dfs(idx, g, uf):
            if not g[idx]:
                if nums[idx] != 1:
                    ans[idx] = 1
                    return 1
                else:
                    ans[idx] = 2
                    return 2
            else:
                m = 1
                for item in g[idx]:
                    m = max(m, dfs(item, g, uf))
                    uf.merge(nums[idx], nums[item])
                root = uf.find(nums[idx])
                for i in range(m, 100001):
                    if root != uf.find(i):
                        ans[idx] = i
                        return i

        dfs(0, g, uf)

        return ans


if __name__ == '__main__':
    sol = Solution()
    parents = [-1, 0, 0, 2]
    nums = [1, 2, 3, 4]
    ret = sol.smallestMissingValueSubtree(parents, nums)
    print(ret)

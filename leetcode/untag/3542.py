from typing import List
from collections import defaultdict

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
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        group = defaultdict(list)
        for idx, val in enumerate(nums):
            if val == 0:
                continue
            group[val].append(idx)

        ans = 0
        hst = set()
        uf = UnionFind(n)
        for val in sorted(group.keys(), reverse=True):
            for idx in group[val]:
                if idx + 1 in hst:
                    uf.merge(idx, idx+1)
                if  idx - 1 in hst:
                    uf.merge(idx, idx-1)
                hst.add(idx)
            vis = set()
            for idx in group[val]:
                vis.add(uf.find(idx))
            ans += len(vis)
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [3, 1, 2, 1]
    ret = sol.minOperations(nums)
    print(ret)

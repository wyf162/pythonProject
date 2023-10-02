# -*- coding : utf-8 -*-
# @Time: 2023/9/16 22:09
# @Author: yefei.wang
# @File: biweek-113-20230916.py
from collections import Counter, defaultdict, deque
from typing import List


class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        sn = list(sorted(nums))
        n = len(nums)
        for i in range(1, n):
            nums.insert(0, nums.pop())
            if sn == nums:
                return i
        return -1

    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        rst = n
        i, j = 0, n >> 1
        while i < (n >> 1) and j < n:
            if nums[i] < nums[j]:
                rst -= 2
                i += 1
                j += 1
            else:
                j += 1
        return rst

    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        hst = Counter()
        cnt = 0
        for x, y in coordinates:
            for i in range(k + 1):
                x1 = x ^ i
                y1 = y ^ (k - i)
                cnt += hst[(x1, y1)]
            hst[(x, y)] += 1
        return cnt

    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(dict)
        for u, v in edges:
            adj[u][v] = 0
            adj[v][u] = 1

        v = 0
        unvis = [True] * n
        q = deque()
        q.append(0)
        unvis[0] = False
        while q:
            x = q.popleft()
            for y in adj[x]:
                if unvis[y]:
                    v += adj[x][y]
                    q.append(y)
                    unvis[y] = False

        ans = [0] * n
        ans[0] = v
        unvis = [True] * n
        q = deque()
        q.append(0)
        unvis[0] = False
        while q:
            x = q.popleft()
            for y in adj[x]:
                if unvis[y]:
                    ans[y] = ans[x] - adj[x][y] + adj[y][x]
                    q.append(y)
                    unvis[y] = False
        return ans


if __name__ == '__main__':
    sol = Solution()
    # n = 4
    # edges = [[2, 0], [2, 1], [1, 3]]
    n = 3
    edges = [[1, 2], [2, 0]]
    ret = sol.minEdgeReversals(n, edges)
    print(ret)

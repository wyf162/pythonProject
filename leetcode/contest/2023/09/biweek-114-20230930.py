# -*- coding : utf-8 -*-
# @Time: 2023/9/30 22:23
# @Author: yefei.wang
# @File: biweek-114-20230930.py
from collections import Counter
from typing import List


class Solution:
    def minOperations1(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = set()
        for i in range(n - 1, -1, -1):
            if nums[i] <= k:
                s.add(nums[i])
            if len(s) == k:
                return n - i

    def minOperations(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 0
        for k, v in cnt.items():
            if v <= 1:
                return -1
            ans += v // 3
            if v % 3:
                ans += 1
        return ans

    def maxSubarrays(self, nums: List[int]) -> int:
        score = nums[0]
        for num in nums:
            score &= num

        n = len(nums)
        cnt = 0
        i = 0
        val = nums[i]
        while i < n:
            if val & nums[i] == score:
                cnt += 1
                if i + 1 >= n:
                    break
                i += 1
                val = nums[i]
            else:
                val &= nums[i]
                i += 1
        return cnt

    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        add = [0] * n

        def dfs(x, fa):
            add[x] += values[x]
            for y in g[x]:
                if y != fa:
                    add[x] += dfs(y, x)
            return add[x]

        dfs(0, -1)
        ans = 1

        def dfs2(x, fa):
            for y in g[x]:
                if y != fa:
                    if add[y] % k == 0:
                        nonlocal ans
                        ans += 1
                    dfs2(y, x)
        dfs2(0, -1)
        return ans


if __name__ == '__main__':
    sol = Solution()
    # nums = [22, 21, 29, 22]
    n = 5
    edges = [[0, 2], [1, 2], [1, 3], [2, 4]]
    values = [2, 8, 2, 4, 4]
    k = 2
    ret = sol.maxKDivisibleComponents(n, edges, values, k)
    print(ret)

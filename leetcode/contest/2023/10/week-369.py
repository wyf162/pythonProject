# -*- coding : utf-8 -*-
# @Time: 2023/10/29 10:05
# @Author: yefei.wang
# @File: week-369.py
from functools import lru_cache
from typing import List


class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        cnt = [0] * 32
        for num in nums:
            for b in range(32):
                if num >> b & 1:
                    cnt[b] += 1

        rst = 0
        for b in range(32):
            if cnt[b] >= k:
                rst |= (1 << b)
        return rst

    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        z1, s1 = 0, 0
        for num in nums1:
            if num == 0:
                z1 += 1
            else:
                s1 += num

        z2, s2 = 0, 0
        for num in nums2:
            if num == 0:
                z2 += 1
            else:
                s2 += num

        if z1 == 0 and s1 < s2 + z2:
            return -1
        if z2 == 0 and s2 < s1 + z1:
            return -1

        return max(s1 + z1, s2 + z2)

    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # 表示将f[i] > k , 变成美丽数组的最少运算次数次数
        # f[i] = f[i-3]
        # f[i-3],f[i-2]

        f = [n * k] * n
        f[0] = max(0, k - nums[0])
        f[1] = max(0, k - nums[1])
        f[2] = max(0, k - nums[2])
        for i in range(3, n):
            f[i] = min(f[i - 3], f[i - 2], f[i - 1]) + max(0, k - nums[i])

        rst = min(f[-1], f[-2], f[-3])
        return rst

    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        mx = [0] * n

        def dfs2(x, fa):
            mx[x] = coins[x]
            for y in g[x]:
                if y != fa:
                    dfs2(y, x)
                    mx[x] = max(mx[x], mx[y])

        dfs2(0, -1)

        @lru_cache(None)
        def dfs(x, fa, b):
            if mx[x] < (1 << b):
                return 0

            rs = 0
            for op in [0, 1]:
                s = 0
                if op == 0:
                    s += (coins[x] >> b) - k
                    for y in g[x]:
                        if y != fa:
                            s += dfs(y, x, b)
                elif op == 1:
                    s += (coins[x] >> b) >> 1
                    for y in g[x]:
                        if y != fa:
                            s += dfs(y, x, b + 1)
                rs = max(rs, s)
            return rs

        rst = dfs(0, -1, 0)
        return rst


if __name__ == '__main__':
    sol = Solution()
    # edges = [[0, 1], [1, 2], [2, 3]]
    # coins = [10, 10, 3, 3]
    # k = 5
    edges = [[1, 0], [2, 1], [3, 1], [2, 4], [5, 4], [6, 3], [6, 7]]
    coins = [9, 9, 5, 5, 7, 9, 6, 9]
    k = 8
    ret = sol.maximumPoints(edges, coins, k)
    print(ret)

    # nums = [2, 3, 0, 0, 2]
    # k = 4
    # ret = sol.minIncrementOperations(nums, k)
    # print(ret)

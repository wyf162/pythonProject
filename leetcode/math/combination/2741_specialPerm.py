# -*- coding : utf-8 -*-
# @Time: 2023/9/16 15:46
# @Author: yefei.wang
# @File: 2741_specialPerm.py

from functools import lru_cache
from typing import List


class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def dfs(i: int, j: int) -> int:
            if i == 0: return 1  # 找到一个特别排列
            res = 0
            for k, x in enumerate(nums):
                if i >> k & 1 and (nums[j] % x == 0 or x % nums[j] == 0):
                    res += dfs(i ^ (1 << k), k)
            return res % MOD

        n = len(nums)
        return sum(dfs(((1 << n) - 1) ^ (1 << j), j) for j in range(n)) % MOD


if __name__ == '__main__':
    sol = Solution()
    sol.specialPerm(1)

# -*- coding: utf-8 -*-
# @Time: 2024/3/13 13:19
# @Author: yfwang
# @File: 3077.py

from typing import List
from itertools import accumulate
from math import inf


class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        n = len(nums)

        f = [[-inf] * (k + 1) for _ in range(n + 1)]
        f[0][0] = 0
        for i in range(n):
            for j in range(1, k + 1):
                if j == 1:
                    f[i + 1][j] = max(0, f[i][j]) + nums[i] * (1 if j % 2 else -1) * (k - j + 1)
                else:
                    f[i + 1][j] = max(f[i][j], f[i][j - 1]) + nums[i] * (1 if j % 2 else -1) * (k - j + 1)

        rst = max(f[i][k] for i in range(1, n + 1))
        return rst


if __name__ == '__main__':
    sol = Solution()
    # nums = [1, 2, 3, -1, 2]
    # nums = [-1, -2, -3]
    nums = [12, -2, -2, -2, -2]
    k = 5
    ret = sol.maximumStrength(nums, k)
    print(ret)

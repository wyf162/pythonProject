# -*- coding : utf-8 -*-
# @Time: 2022/7/17 21:25
# @Author: yefei.wang
# @File: 1658_min_operations.py
from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        ret = -1

        def dfs(l, r, x):
            if x == 0:
                nonlocal ret
                if ret<0:
                    ret = l + n - r - 1
                else:
                    ret = min(ret, l+n-r-1)
            if x < 0 or l > r:
                return
            else:
                dfs(l + 1, r, x - nums[l])
                dfs(l, r - 1, x - nums[r])

        dfs(0, n - 1, x)

        return ret


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 1, 4, 2, 3]
    x = 5
    ret = sol.minOperations(nums, x)
    print(ret)

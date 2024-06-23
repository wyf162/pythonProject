# -*- coding : utf-8 -*-
# @Time: 2024/6/22 22:29
# @Author: yefei.wang
# @File: C.py

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i, x in enumerate(nums):
            if x == 0:
                if ans % 2:
                    continue
                else:
                    ans += 1
            else:
                if ans % 2:
                    ans += 1
                else:
                    continue
        return ans


if __name__ == '__main__':
    sol = Solution()
    # nums = [0, 1, 1, 1, 0, 0]
    # nums = [0, 1, 1, 1]
    nums = [1, 0, 0, 0]
    ret = sol.minOperations(nums)
    print(ret)
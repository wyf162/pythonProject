# -*- coding : utf-8 -*-
# @Time: 2023/12/31 10:33
# @Author: yefei.wang
# @File: A.py
from typing import List


class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] % 2 == 0 and nums[j] % 2 == 0:
                    return True
        return False


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2]
    ret = sol.hasTrailingZeros(nums)
    print(ret)

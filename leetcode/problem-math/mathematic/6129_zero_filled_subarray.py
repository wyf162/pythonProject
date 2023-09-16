# -*- coding : utf-8 -*-
# @Time: 2022/7/24 9:42
# @Author: yefei.wang
# @File: 6129_zero_filled_subarray.py
from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        cnt = 0
        for i, num in enumerate(nums):
            if num==0:
                cnt += 1
            else:
                ans += ((cnt+1)*cnt)//2
                cnt = 0
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [0, 0, 0, 2, 0, 0]
    ret = sol.zeroFilledSubarray(nums)
    print(ret)

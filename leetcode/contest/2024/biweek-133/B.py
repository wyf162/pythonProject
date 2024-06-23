# -*- coding : utf-8 -*-
# @Time: 2024/6/22 22:29
# @Author: yefei.wang
# @File: B.py

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        i = 0
        while i < n:
            if nums[i] == 1:
                i += 1
            else:
                ans += 1
                if i + 2 < n:
                    nums[i + 1] = 1 ^ nums[i + 1]
                    nums[i + 2] = 1 ^ nums[i + 2]
                else:
                    ans = -1
                    break
                i += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [0, 1, 1, 1, 0, 0]
    nums = [0, 1, 1, 1]
    ret = sol.minOperations(nums)
    print(ret)


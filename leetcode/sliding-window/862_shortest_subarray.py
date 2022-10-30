# _*_ coding: utf-8 _*_
# @Time : 2022/10/26 9:56 PM 
# @Author : yefe
# @File : 862_shortest_subarray

from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        ans = 999999
        i = 0
        j = 0
        n = len(nums)
        s = 0

        while j < n:
            s += nums[j]
            while s >= k:
                ans = min(ans, j - i + 1)
                s -= nums[i]
                i += 1
            j += 1

        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [84,-37,32,40,95]
    k = 167
    ret = sol.shortestSubarray(nums, k)
    print(ret)

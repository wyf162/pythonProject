# _*_ coding: utf-8 _*_
# @Time : 2023/01/28 10:46 PM 
# @Author : yefe
# @File : 1664_ways_to_make_fair

from typing import List


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        odd_pre_sum = [0]
        event_pre_sum = [0]
        for i in range(n):
            if i % 2 == 1:
                odd_pre_sum.append(odd_pre_sum[-1] + nums[i])
            else:
                odd_pre_sum.append(odd_pre_sum[-1] + 0)
        for i in range(n):
            if i % 2 == 0:
                event_pre_sum.append(event_pre_sum[-1] + nums[i])
            else:
                event_pre_sum.append(event_pre_sum[-1] + 0)

        ans = 0
        for i in range(n):
            odds = odd_pre_sum[i] + event_pre_sum[-1] - event_pre_sum[i + 1]
            events = event_pre_sum[i] + odd_pre_sum[-1] - odd_pre_sum[i + 1]
            if odds == events:
                ans += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [2, 1, 6, 4]
    ret = sol.waysToMakeFair(nums)
    print(ret)

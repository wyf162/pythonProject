# _*_ coding: utf-8 _*_
# @Time : 2022/05/22 2:21 PM 
# @Author : yefe
# @File : 1856_max_sum_min_product

from typing import List


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]
        pre.append(0)

        left = [-1] * n
        stk = []
        for i in range(n):
            while stk and nums[stk[-1]] >= nums[i]:
                stk.pop()
            if stk:
                left[i] = stk[-1]
            stk.append(i)

        right = [n] * n
        stk = []
        for i in range(n - 1, -1, -1):
            while stk and nums[stk[-1]] > nums[i]:
                stk.pop()
            if stk:
                right[i] = stk[-1]
            stk.append(i)

        prd = nums[0] * nums[0]
        for i in range(n):
            l, r = left[i]+1, right[i]-1
            val = (pre[r+1] - pre[l]) * nums[i]
            prd = max(prd, val)
        return prd % 1000000007


if __name__ == '__main__':
    # nums = [1, 2, 3, 2]
    nums = [1, 2, 3]
    ret = Solution().maxSumMinProduct(nums)
    print(ret)

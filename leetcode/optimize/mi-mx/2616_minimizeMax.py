# -*- coding : utf-8 -*-
# @Time: 2023/9/16 14:01
# @Author: yefei.wang
# @File: 2616_minimizeMax.py
from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        nums.sort()

        # difference value
        def check(dv):
            cnt = 0
            i = 0
            while i < n - 1:
                if nums[i + 1] - nums[i] <= dv:
                    cnt += 1
                    i += 2
                else:
                    i += 1
            return cnt

        l, r = 0, 10 ** 9 + 1
        while l <= r:
            m = (l + r) >> 1
            if check(m) < p:
                l = m + 1
            else:
                rst = m
                r = m - 1
        return rst


if __name__ == '__main__':
    sol = Solution()
    # nums = [10, 1, 2, 7, 1, 3]
    # p = 2
    nums = [4, 2, 1, 2]
    p = 1
    ret = sol.minimizeMax(nums, p)
    print(ret)

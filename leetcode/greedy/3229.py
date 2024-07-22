# -*- coding: utf-8 -*-
# @Time: 2024/7/22 14:49
# @Author: yfwang
# @File: 3229.py

from itertools import pairwise
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            nums[i] -= target[i]
        print(nums)

        def compute(arr):
            if not arr:
                return 0
            elif arr[0] > 0:
                ret = 0
                pre = 0
                for a in arr:
                    ret += max(a - pre, 0)
                    pre = a
                return ret
            else:
                ret = 0
                pre = 0
                for a in arr:
                    ret += max(0 - (pre + a), 0)
                    pre = abs(a)
                return ret

        ans = 0
        group = []
        for x in nums:
            if x == 0:
                tmp = compute(group)
                ans += tmp
                group = []
            else:
                if not group or group[-1] * x > 0:
                    group.append(x)
                else:
                    tmp = compute(group)
                    ans += tmp
                    group = [x]
        tmp = compute(group)
        ans += tmp
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [3, 5, 1, 2]
    target = [4, 6, 2, 4]
    ret = sol.minimumOperations(nums, target)
    print(ret)

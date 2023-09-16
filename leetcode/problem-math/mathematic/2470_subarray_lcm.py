# _*_ coding: utf-8 _*_
# @Time : 2023/01/03 9:26 PM 
# @Author : yefe
# @File : 2470_subarray_lcm

from math import lcm
from typing import List


class Solution2:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        ans, n = 0, len(nums)
        for i in range(n):
            res = 1
            for j in range(i, n):
                res = lcm(res, nums[j])
                if k % res:
                    break
                if res == k:
                    ans += 1
        return ans


class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        ans = 0
        a = []
        i0 = -1
        for i, x in enumerate(nums):
            if k % x:
                a = []
                i0 = i
                continue
            a.append([x, i])
            j = 0
            for p in a:
                p[0] = lcm(p[0], x)
                if a[j][0] != p[0]:
                    j += 1
                    a[j] = p
                else:
                    a[j][1] = p[1]
            del a[j + 1:]
            if a[0][0] == k:
                ans += a[0][1] - i0
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [2, 3, 3, 6, 6]
    k = 6
    ret = sol.subarrayLCM(nums, k)
    print(ret)

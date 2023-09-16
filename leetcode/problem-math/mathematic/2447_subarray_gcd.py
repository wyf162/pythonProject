# _*_ coding: utf-8 _*_
# @Time : 2023/01/04 9:56 PM 
# @Author : yefe
# @File : 2447_subarray_gcd

from math import gcd
from typing import List


class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ans = 0
        a = []
        i0 = -1
        for i, num in enumerate(nums):
            if num % k:
                a = []
                i0 = i
                continue
            a.append([num, i])
            j = 0
            for p in a:
                p[0] = gcd(p[0], num)
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
    nums = [9, 3, 1, 2, 6, 3]
    k = 3
    ret = sol.subarrayGCD(nums, k)
    print(ret)

# _*_ coding: utf-8 _*_
# @Time : 2022/10/23 5:28 PM 
# @Author : yefe
# @File : 6234_subarray_gcd

from math import gcd
from typing import List


class Solution:
    def subarrayGCD2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g % k: break
                if g == k: ans += 1
        return ans

    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ans = 0
        a = []
        i0 = -1
        for i, x in enumerate(nums):
            if x % k:
                a = []
                i0 = i
                continue
            a.append([x, i])

            j = 0
            for p in a:
                p[0] = gcd(p[0], x)
                if a[j][0] == p[0]:
                    a[j][1] = p[1]
                else:
                    j += 1
                    a[j] = p
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


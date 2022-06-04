# _*_ coding: utf-8 _*_
# @Time : 2022/06/04 3:26 PM 
# @Author : yefe
# @File : 1879_minimum_XOR_sum
from typing import List


class Solution2:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:

        self.all_nums1 = []
        nums1.sort()
        check = [0 for i in range(len(nums1))]
        self.backtrack([], nums1, check)
        return min([self.calculate_xor(nums1, nums2) for nums1 in self.all_nums1])

    def backtrack(self, sol, nums, check):
        if len(sol) == len(nums):
            self.all_nums1.append(sol)
            return

        for i in range(len(nums)):
            if check[i] == 1:
                continue
            if i > 0 and nums[i] == nums[i - 1] and check[i - 1] == 0:
                continue
            check[i] = 1
            self.backtrack(sol + [nums[i]], nums, check)
            check[i] = 0

    def calculate_xor(self, nums1, nums2):
        return sum(x ^ y for x, y in zip(nums1, nums2))


class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        MAX = 1 << 32
        n = len(nums1)
        f = [MAX] * (1 << n)
        f[0] = 0

        for mask in range(1, 1 << n):
            c = mask.bit_count()
            for i in range(n):
                if mask & (1 << i):
                    f[mask] = min(f[mask], f[mask ^ (1 << i)] + (nums1[c - 1] ^ nums2[i]))
        return f[(1 << n) - 1]


if __name__ == '__main__':
    sol = Solution()
    nums1 = [1, 2]
    nums2 = [2, 3]
    ret = sol.minimumXORSum(nums1, nums2)
    print(ret)

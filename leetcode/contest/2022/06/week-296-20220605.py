# _*_ coding: utf-8 _*_
# @Time : 2022/06/05 10:29 AM 
# @Author : yefe
# @File : week-296-20220605
from typing import List


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            n = len(nums)
            new_nums = [0] * (n >> 1)
            for i in range(n >> 1):
                if i % 2 == 0:
                    new_nums[i] = min(nums[2 * i], nums[2 * i + 1])
                else:
                    new_nums[i] = max(nums[2 * i], nums[2 * i + 1])
            nums = new_nums
        return nums[0]

    def partitionArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        i = 0
        s = nums[i]
        i += 1
        ans = 1
        while i < n:
            if nums[i] - s <= k:
                i += 1
            else:
                s = nums[i]
                i += 1
                ans += 1
        return ans

    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        hst = {v: i for i, v in enumerate(nums)}
        for operation in operations:
            bf, af = operation
            idx = hst[bf]
            nums[idx] = af
            hst[af] = idx
        return nums


if __name__ == '__main__':
    sol = Solution()
    # nums = [1, 2, 4, 6]
    # operations = [[1, 3], [4, 7], [6, 1]]
    # ret = sol.arrayChange(nums, operations)
    # print(ret)

    # nums = [3, 6, 1, 2, 5]
    # k = 2
    # ret = sol.partitionArray(nums, k)
    # print(ret)

    # nums = [1, 3, 5, 2, 4, 8, 2, 2]
    # ret = sol.minMaxGame(nums)
    # print(ret)

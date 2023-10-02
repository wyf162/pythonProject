# -*- coding : utf-8 -*-
# @Time: 2022/6/28 20:42
# @Author: yefei.wang
# @File: 324_wiggle_sort.py
from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        arr = sorted(nums)
        x = (n + 1) // 2
        j, k = x - 1, n - 1
        for i in range(0, n, 2):
            nums[i] = arr[j]
            if i + 1 < n:
                nums[i + 1] = arr[k]
            j -= 1
            k -= 1


if __name__ == '__main__':
    sol = Solution()
    # nums = [1, 3, 2, 2, 3, 1]
    # nums = [1,1,2,1,2,2,1]
    nums = [4,5,5,6]
    sol.wiggleSort(nums)
    print(nums)

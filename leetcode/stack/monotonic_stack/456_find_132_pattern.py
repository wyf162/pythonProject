# -*- coding : utf-8 -*-
# @Time: 2022/7/17 17:04
# @Author: yefei.wang
# @File: 456_find_132_pattern.py

from typing import List


class Solution(object):
    def find132pattern(self, nums: List[int]):
        N = len(nums)
        leftMin = [float("inf")] * N
        for i in range(1, N):
            leftMin[i] = min(leftMin[i - 1], nums[i - 1])
        stack = []
        for j in range(N - 1, -1, -1):
            numsk = float("-inf")
            while stack and stack[-1] < nums[j]:
                numsk = stack.pop()
            if leftMin[j] < numsk:
                return True
            stack.append(nums[j])
        return False


if __name__ == '__main__':
    sol = Solution()
    nums = [3, 1, 4, 2]
    ret = sol.find132pattern(nums)
    print(ret)

# -*- coding : utf-8 -*-
# @Time: 2023/10/8 10:31
# @Author: yefei.wang
# @File: week-366.py
from collections import Counter
from typing import List


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        s1, s2 = 0, 0
        for i in range(1, n):
            if i % m:
                s1 += i
            else:
                s2 += i
        return s1 - s2

    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        n = len(processorTime)
        ans = None
        for i in range(n):
            if ans is None:
                ans = tasks[4 * i] + processorTime[i]
            else:
                ans = max(ans, tasks[4 * i] + processorTime[i])
        return ans

    def minOperations(self, s1: str, s2: str, x: int) -> int:
        pass

    def maxSum(self, nums: List[int], k: int) -> int:
        B = 32
        bits = [0] * B
        for num in nums:
            for b in range(B):
                if (num >> b) & 1:
                    bits[b] += 1

        ans = 0
        mod = 10**9 + 7
        for i in range(k):
            num = 0
            for b in range(B):
                if bits[b] > 0:
                    bits[b] -= 1
                    num |= (1<<b)
            ans += num*num
            ans %= mod
        return ans


if __name__ == '__main__':
    sol = Solution()
    # nums = [2, 6, 5, 8]
    # k = 2
    nums = [4, 5, 4, 7]
    k = 3
    ret = sol.maxSum(nums, k)
    print(ret)
# -*- coding : utf-8 -*-
# @Time: 2024/2/18 15:09
# @Author: yefei.wang
# @File: 100205.py
import copy
from collections import defaultdict
from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        f = defaultdict(int)
        for x in nums:
            f[x + 1] = f[x] + 1
            f[x] = f[x - 1] + 1
        return max(f.values())


if __name__ == '__main__':
    sol = Solution()
    nums = [2, 1, 5, 1, 1]
    ret = sol.maxSelectedElements(nums)
    print(ret)

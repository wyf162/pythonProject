# -*- coding : utf-8 -*-
# @Time: 2024/5/19 10:33
# @Author: yefei.wang
# @File: B.py

from typing import List
from itertools import accumulate


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        f = [0] * n
        for i in range(1, n):
            if nums[i - 1] % 2 == 0 and nums[i] % 2 == 0:
                f[i] = 1
            elif nums[i - 1] % 2 == 1 and nums[i] % 2 == 1:
                f[i] = 1
            else:
                f[i] = 0
        pf = list(accumulate(f, initial=0))
        ans = []
        for l, r in queries:
            if pf[r + 1] - pf[l + 1] == 0:
                ans.append(True)
            else:
                ans.append(False)
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [4, 3, 1, 6]
    queries = [[0, 2], [2, 3]]
    ret = sol.isArraySpecial(nums, queries)
    print(ret)

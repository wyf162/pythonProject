# -*- coding: utf-8 -*-
# @Time: 2024/3/7 16:04
# @Author: yfwang
# @File: 3049.py

from bisect import bisect_left
from heapq import heappop, heappush
from typing import List


class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        n, m = len(nums), len(changeIndices)
        tot = n + sum(nums)
        first_t = [-1] * n
        for t in range(m - 1, -1, -1):
            first_t[changeIndices[t]] = t

        def check(mx):
            cnt = 0
            slow = tot
            h = []
            for t in range(mx - 1, -1, -1):
                i = changeIndices[t] - 1
                v = nums[i]
                if v <= 1 or t != first_t[i]:
                    cnt += 1
                    continue
                if cnt == 0:
                    if not h or v <= h[0]:
                        cnt += 1
                        continue
                    slow += heappop(h)
                    cnt += 2
                slow -= v + 1
                cnt -= 1
                heappush(h, v)
            return cnt >= slow

        ans = n + bisect_left(range(n, m + 1), True, key=check)
        return -1 if ans > m else ans


if __name__ == '__main__':
    sol = Solution()
    nums = [0, 0, 1, 2]
    changeIndices = [1, 2, 1, 2, 1, 2, 1, 2]
    ret = sol.earliestSecondToMarkIndices(nums, changeIndices)
    print(ret)

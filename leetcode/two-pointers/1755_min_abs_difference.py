# -*- coding : utf-8 -*-
# @Time: 2022/8/7 19:36
# @Author: yefei.wang
# @File: 1755_min_abs_difference.py
from typing import List


class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        half = n // 2
        ls = half
        rs = n - half

        lsum = [0] * (1 << ls)
        for i in range(1 << ls):
            for j in range(ls):
                if (1 << j) & i:
                    lsum[i] = lsum[i - (1 << j)] + nums[j]
                    break

        rsum = [0] * (1 << rs)
        for i in range(1 << rs):
            for j in range(rs):
                if (1 << j) & i:
                    rsum[i] = rsum[i - (1 << j)] + nums[ls+j]
                    break

        lsum.sort()
        rsum.sort()

        ret = 1 << 40

        for x in lsum:
            ret = min(ret, abs(goal - x))

        for x in rsum:
            ret = min(ret, abs(goal - x))

        i = 0
        j = (1 << rs) - 1
        while i < (1 << ls) and j >= 0:
            s = lsum[i] + rsum[j]
            ret = min(ret, abs(goal - s))
            if s > goal:
                j -= 1
            else:
                i += 1
        return ret


if __name__ == '__main__':
    sol = Solution()
    nums = [5, -7, 3, 5]
    goal = 6
    ret = sol.minAbsDifference(nums, goal)
    print(ret)

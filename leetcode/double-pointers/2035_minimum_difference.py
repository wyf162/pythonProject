# -*- coding : utf-8 -*-
# @Time: 2022/8/7 22:37
# @Author: yefei.wang
# @File: 2035_minimum_difference.py
from typing import List
from collections import defaultdict


class Solution:
    def minimumDifference2(self, nums: List[int]) -> int:
        # min(abs(s-2x))
        s = sum(nums)

        ans = 1 << 31

        def dfs(i, cnt, x):
            nonlocal ans
            if cnt * 2 == len(nums):
                ans = min(ans, abs(s - 2 * x))
            if i == len(nums) or cnt * 2 > len(nums):
                return
            dfs(i + 1, cnt, x)
            dfs(i + 1, cnt + 1, x + nums[i])

        dfs(0, 0, 0)
        return ans

    def minimumDifference(self, nums: List[int]) -> int:
        s = sum(nums)
        n = len(nums)
        half = n >> 1
        ls = rs = half

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
                    rsum[i] = rsum[i - (1 << j)] + nums[ls + j]
                    break

        lhst = defaultdict(list)
        rhst = defaultdict(list)
        for i in range(1 << ls):
            k = bin(i).count('1')
            lhst[k].append(lsum[i])
            rhst[k].append(rsum[i])

        for k, v in lhst.items():
            v.sort()
        for k, v in rhst.items():
            v.sort()

        ans = min(abs(s - 2 * lhst[half][0]), abs(s - 2 * rhst[half][0]))

        for k in range(1, half):
            i = 0
            j = len(rhst[half - k])-1
            while i < len(lhst[k]) and j >= 0:
                h = lhst[k][i] + rhst[half - k][j]
                ans = min(ans, abs(s - 2 * h))
                if s < 2 * h:
                    j -= 1
                else:
                    i += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    # nums = [2,-1,0,4,-2,-9]
    # nums = [3, 9, 7, 3]
    # nums = [36, -36]
    nums = [7772197, 4460211, -7641449, -8856364, 546755, -3673029, 527497, -9392076, 3130315, -5309187, -4781283,
            5919119, 3093450, 1132720, 6380128, -3954678, -1651499, -7944388, -3056827, 1610628, 7711173, 6595873,
            302974, 7656726, -2572679, 0, 2121026, -5743797, -8897395, -9699694]

    ret = sol.minimumDifference(nums)
    print(ret)

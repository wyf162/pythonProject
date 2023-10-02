# -*- coding : utf-8 -*-
# @Time: 2023/9/17 10:30
# @Author: yefei.wang
# @File: week-363.py
from typing import List

from numpy import math


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            if bin(i).count('1') == k:
                ans += nums[i]
        return ans

    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        select_number = 0
        ans = 0
        for i in range(n - 1):
            select_number += 1
            if select_number > nums[i] and select_number < nums[i + 1]:
                ans += 1
        if n > nums[-1]:
            ans += 1
        if 0 < nums[0]:
            ans += 1
        return ans

    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int],
                          cost: List[int]) -> int:

        def check(m, idx_machine):
            total_cost = 0
            for i, cp in enumerate(composition[idx_machine]):
                need = m * cp - stock[i]
                if need > 0:
                    total_cost += need * cost[i]
            return total_cost

        ans = [0] * k
        for idx_machine in range(k):
            l, r = 0, 10 ** 9
            while l <= r:
                m = (l + r) >> 1
                if check(m, idx_machine) <= budget:
                    ans[idx_machine] = m
                    l = m + 1
                else:
                    r = m - 1
        return max(ans)

    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        # print(n)
        k = int(math.sqrt(n))
        ans = 0
        for i in range(1, k + 1):
            ans += nums[i * i - 1]

        ans = max(ans, max(nums))

        for i in range(1, (n >> 1) + 1, 1):
            ii = i * i
            for x in range(1, ii + 1):
                y = ii // x
                if y <= x:
                    break
                if ii % x == 0 and x <= n and y <= n:
                    ans = max(ans, nums[x - 1] + nums[y - 1])

        return ans


if __name__ == '__main__':
    sol = Solution()
    # nums = [6, 0, 3, 3, 6, 7, 2, 7]
    # nums = [0, 4, 4, 4, 4, 4, 2]
    # nums = [8, 7, 3, 5, 7, 2, 4, 9]
    # nums = [5, 10, 3, 10, 1, 13, 7, 9, 4]
    nums = [33969, 24796, 64674, 1378, 12216, 70450, 58226, 71401, 64921, 95169, 5383, 47175, 24892, 4130, 74768, 54172,
            31625, 781067253, 25106074, 57175513, 1, 240671921, 95079775, 520810854, 1, 344117679, 575539902, 678498979,
            443032835, 685824944, 152895587, 1, 784748873, 667662128, 109570671, 654252351, 763152321, 716977360,
            750506142, 574160523, 629177330, 386270189, 317284125, 668042248, 620709633, 325542831, 407572002,
            610115189, 320351721, 412659468, 1, 1, 527228178, 359984365, 1, 149339083, 1, 136493305, 100938728,
            754000216, 5751596, 582609624, 275055892, 114306242, 21277447, 91154507, 745223795, 663228215, 1, 474272254,
            39451110]
    ret = sol.maximumSum(nums)
    print(ret)
# 1193822919

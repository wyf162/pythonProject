# -*- coding : utf-8 -*-
# @Time: 2022/6/11 22:25
# @Author: yefei.wang
# @File: biweek-80-20220611.py
import math
from typing import List
import bisect
from collections import defaultdict


class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        big = False
        small = False
        number = False
        special = False
        repeat = True
        length = len(password) >= 8

        for i, a in enumerate(password):
            if 'a' <= a <= 'z':
                small = True
            elif 'A' <= a <= 'Z':
                big = True
            elif '0' <= a <= '9':
                number = True
            elif a in "!@#$%^&*()-+":
                special = True

            if i >= 1 and password[i] == password[i - 1]:
                repeat = False

        return big and small and number and special and repeat and length

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()

        m = len(potions)
        n = len(spells)
        rets = [0] * n
        for idx, spell in enumerate(spells):
            k = math.ceil(success / spell)
            l = bisect.bisect_left(potions, k)
            rets[idx] = m - l

        return rets

    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        if len(sub) > len(s):
            return False
        hst = defaultdict(set)
        for x, y in mappings:
            hst[x].add(y)

        n = len(s)
        m = len(sub)
        for i in range(n - m + 1):
            flag = True
            for j in range(m):
                if s[i + j] == sub[j] or s[i + j] in hst[sub[j]]:
                    continue
                else:
                    flag = False
                    break
            if flag:
                return True
        return False

    def countSubarrays2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]
        dp = [0] * n
        for i in range(n):
            t = self.search(pre[:i + 2], k)
            dp[i] = i - t + 1
        return sum(dp)

    def search(self, pre, k):
        n = len(pre) - 1
        l, r = 0, len(pre)
        while l <= r:
            m = (l + r) // 2
            if (pre[-1] - pre[m]) * (n - m) < k:
                r = m - 1
            else:
                l = m + 1
        return l

    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i, j = 0, 0
        s = 0
        cnt = 0
        while j < n:
            s += nums[j]
            if s * (j - i + 1) < k:
                print(j, i, j-i)
                cnt += j-i+1
            else:

                while i < n and s * (j - i + 1) >= k:
                    s -= nums[i]
                    i += 1
                print(j, i, j - i)
                cnt += j - i+1
            j += 1
        return cnt


if __name__ == '__main__':
    sol = Solution()

    # nums = [2, 1, 4, 3, 5]
    # k = 10
    nums = [1, 1, 1]
    k = 5
    ret = sol.countSubarrays(nums, k)
    print(ret)

    # s = "fool3e7bar"
    # sub = "leet"
    # mappings = [["e", "3"], ["t", "7"], ["t", "8"]]
    #
    # ret = sol.matchReplacement(s, sub, mappings)
    # print(ret)

    # spells = [5, 1, 3]
    # potions = [1, 2, 3, 4, 5]
    # success = 7

    # spells = [3, 1, 2]
    # potions = [8, 5, 8]
    # success = 16
    # rets = sol.successfulPairs(spells, potions, success)
    # print(rets)

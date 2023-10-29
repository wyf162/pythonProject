# -*- coding : utf-8 -*-
# @Time: 2023/10/22 10:29
# @Author: yefei.wang
# @File: week-368.py
from typing import List
from collections import Counter
from functools import lru_cache


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        MX = 0x3f3f3f3f
        lmi = [MX] * n
        for i in range(1, n):
            lmi[i] = min(nums[i - 1], lmi[i - 1])

        rmi = [MX] * n
        for i in range(n - 2, -1, -1):
            rmi[i] = min(nums[i + 1], rmi[i + 1])

        ans = MX
        for i in range(1, n - 1):
            if lmi[i] < nums[i] and rmi[i] < nums[i]:
                ans = min(ans, lmi[i] + nums[i] + rmi[i])
        return ans if ans < MX else -1

    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        xs = list(sorted(cnt.values()))
        if len(xs) == 1:
            return 1

        def check(m):
            m1, m2 = m, m + 1
            for x in xs:
                a, b = x // m1, x % m1
                if b > a:
                    return False
            return True

        ans = 1
        l, r = 1, 2 * xs[0] + 1
        while l <= r:
            m = (l + r) // 2
            if check(m):
                ans = m
                l = m + 1
            else:
                r = m - 1
        rst = 0
        for x in xs:
            rst += (x + ans) // (ans + 1)
        return rst

    def minimumChanges(self, s: str, K: int) -> int:
        MX = len(s)

        @lru_cache(None)
        def palindrome(t):
            l, r = 0, len(t) - 1
            ans = 0
            while l < r:
                ans += int(t[l] != t[r])
                l += 1
                r -= 1
            return ans

        @lru_cache(None)
        def half_palindrome(t):
            if len(t) == 1:
                return MX

            ans = len(t)
            for d in range(1, len(t)):
                if len(t) % d:
                    continue
                tt = [''] * d
                for i in range(len(t)):
                    j = i % d
                    tt[j] += t[i]
                tmp = 0
                for st in tt:
                    tmp += palindrome(st)
                ans = min(ans, tmp)
                if ans == 0:
                    return ans
            return ans

        n = len(s)
        dp = [[n] * K for i in range(n)]
        # f[i][j] 表示把i分成j个半回文串的最少修改次数
        for i in range(n):
            dp[i][0] = half_palindrome(s[:i + 1])

        for i in range(2, n):
            for j in range(0, i, 2):
                for k in range(1, min(K, i//2 + 1)):
                    dp[i][k] = min(dp[i][k], dp[j][k - 1] + half_palindrome(s[j + 1:i + 1]))
                    if dp[-1][-1] == 0:
                        return dp[-1][-1]
        return dp[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    # s = "abcdef"
    # k = 2
    # s = "aabbaa"
    # k = 3
    # s = 'abc'
    # k = 1
    s = 'acba'
    k = 2
    ret = sol.minimumChanges(s, k)
    print(ret)
    # nums = [10, 10, 10, 3, 1, 1]
    # nums = [3, 2, 3, 2, 3]
    # nums = [1, 1, 1, 1, 1]
    # nums = [2, 3, 3, 3, 2, 3, 2, 3, 2]
    # ret = sol.minGroupsForValidAssignment(nums)
    # print(ret)
    # nums = [5, 4, 8, 7, 10, 2]
    # nums = [6, 5, 4, 3, 4, 5]
    # ret = sol.minimumSum(nums)
    # print(ret)

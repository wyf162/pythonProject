# -*- coding : utf-8 -*-
# @Time: 2023/10/28 22:21
# @Author: yefei.wang
# @File: biweek-116.py
from collections import Counter
from typing import List


class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(0, n, 2):
            if s[i] != s[i + 1]:
                ans += 1
        return ans

    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [[0 for j in range(target + 1)] for i in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(n):
            for j in range(target, 0, -1):
                if j - nums[i] >= 0 and dp[i][j - nums[i]]:
                    dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - nums[i]] + 1)
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])

        return dp[-1][-1] - 1

    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        mod = 10 ** 9 + 7
        m = len(set(nums))
        d = [0] * (m + 2)
        cnt = Counter()

        for i, num in enumerate(nums):
            if i not in cnt:
                d[0] += 1
                d[len(cnt) + 1] -= 1
                cnt[num] = i

            else:
                li = cnt[num]
                d[0] += 1
                c = len(set(nums[li: i]))
                d[c - 1] += 1
                d[c] -= 1
                d[len(cnt) + 1] -= 1
                cnt[num] = i
            s = [0]
            for i in range(m):
                s.append(s[-1] + d[i])
            print(s)

        s = [0]
        for i in range(m):
            s.append(s[-1] + d[i])
        # print(s)

        rst = 0
        for i in range(1, m + 1):
            rst += s[i] * i * i
            rst %= mod
        return rst

    def sumCounts2(self, nums: List[int]) -> int:
        n = len(nums)
        rst = 0
        mod = 10 ** 9 + 7
        for i in range(n):
            for j in range(i + 1, n + 1):
                c = len(set(nums[i:j]))
                # print(i, j, c)
                rst += c * c
                rst %= mod
        return rst


if __name__ == '__main__':
    sol = Solution()
    nums = [2, 1, 2, 3, 4]
    ret = sol.sumCounts(nums)
    print(ret)
    # nums = [1, 2, 3, 4, 5]
    # target = 9
    # nums = [4, 1, 3, 2, 1, 5]
    # target = 7
    # nums = [1, 2]
    # target = 10
    # ret = sol.lengthOfLongestSubsequence(nums, target)
    # print(ret)
